from userbot import bot
from telethon import events
from userbot.utils import command, remove_plugin, load_module
from var import Var
import importlib
from pathlib import Path
from userbot import LOAD_PLUG
import sys
import asyncio
import traceback
import os
import userbot.utils
from datetime import datetime

DELETE_TIMEOUT = 10

thumb_image_path = "https://telegra.ph/file/5f441cf7e1186fdc8048a.png"

@command(pattern="^.install", outgoing=True)
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(  # pylint:disable=E0602
                await event.get_reply_message(),
                "userbot/plugins/"  # pylint:disable=E0602
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.edit("Installed Plugin `{}`".format(os.path.basename(downloaded_file_name)))
            else:
                os.remove(downloaded_file_name)
                await event.edit("Errors! Cannot install this plugin. It might be an Installed Plugin")
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


def progress_callback(current, total):
    print('Uploaded', current, 'out of', total,
          'bytes: {:.2%}'.format(current / total))

@command(pattern="^.send (?P<shortname>\w+)$", outgoing=True)
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    thumb = thumb_image_path
    EverythingSuckz = "_Reply_ `,install` _to load this Plugin/Module Temporarly_"
    input_str = event.pattern_match["shortname"]
    the_plugin_file = "./userbot/plugins/{}.py".format(input_str)
    start = datetime.now()
    await event.client.send_file(  # pylint:disable=E0602
        event.chat_id,
        the_plugin_file,
        thumb=thumb,
        progress_callback=progress_callback,
        caption=EverythingSuckz,
        force_document=True,
        allow_cache=False,
        reply_to=event.message.reply_to_msg_id
    )
    end = datetime.now()
    time_taken_in_ms = (end - start).seconds
    await event.edit("Uploaded {} in {} seconds".format(input_str, time_taken_in_ms))
    await asyncio.sleep(5)
    await event.delete()

@command(pattern="^.unload (?P<shortname>\w+)$", outgoing=True)
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"Unloaded {shortname} successfully")
    except Exception as e:
        await event.edit("Successfully unload {shortname}\n{}".format(shortname, str(e)))

@command(pattern="^.load (?P<shortname>\w+)$", outgoing=True)
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except:
            pass
        load_module(shortname)
        await event.edit(f"Successfully loaded {shortname}")
    except Exception as e:
        await event.edit(f"Could not load {shortname} because of the following error.\n{str(e)}")

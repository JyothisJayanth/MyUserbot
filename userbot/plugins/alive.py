"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# by @WhySooSerious

import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP, ALIVE_PIC
from userbot.utils import admin_cmd
from telethon import version
from platform import python_version, uname
from userbot.__init__ import StartTime
from datetime import datetime
import time

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"



ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
if ALIVE_PIC is None:
  ALIVE_GIF = "https://telegra.ph/file/a6c374a64cb906ebdc4d6.mp4"
else:
  ALIVE_GIF = ALIVE_PIC


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time



    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))


mod_caption = "**Your Userbot is running**\n\n"
mod_caption += "`SYSTEM STATUS\n\n`"
mod_caption += f"`Python: {python_version()}\n`"
mod_caption += f"`Telethon version: {version.__version__}\n`"
mod_caption += f"`Ping speed: {ms}\nUserbot Uptime: {uptime}`\n"
mod_caption += "`Server HQ` : [Switch SUPERNAP](https://www.switch.com/about), LA\n`"
mod_caption += "`Database : Amazon Web Services`\n\n"
mod_caption += "`My Rightful OWNER`: **WRENCH**\n\n"
mod_caption += "[@WhySooSerious](https://github.com/JyothisJayanth)"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete() 
    await borg.send_file(alive.chat_id, ALIVE_GIF,caption=mod_caption)

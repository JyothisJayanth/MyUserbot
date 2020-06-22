"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
PM_IMG = "https://telegra.ph/file/fd2b0fabaae61936f3442.jpg"
pm_caption = "`Your Userbot is running\n\nTelethon version: 6.9.0\nPython: 3.7.3\n\n`"
pm_caption += f"`My Rightful OWNER`: {DEFAULTUSER}\n\n"
pm_caption += f"`Server HQ` : [Switch SUPERNAP Campus, Las Vegas](https://www.switch.com/about)\n"
pm_caption += "`Database : Amazon Web Services \n\nAlways with you, MY MASTER!`\n"
pm_caption += "[@WhySooSerious](https://github.com/JyothisJayanth)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete() 
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)

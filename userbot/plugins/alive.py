"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
PM_GIF = "https://telegra.ph/file/a6c374a64cb906ebdc4d6.mp4"
pm_caption = "`Your Userbot is running\n\nTelethon version: 6.9.0\nPython: 3.7.3\n\n`"
pm_caption += "`My Rightful OWNER`: **WRENCH**\n\n"
pm_caption += "`Server HQ` : [Switch SUPERNAP, LA](https://www.switch.com/about)\n"
pm_caption += "`Database : Amazon Web Services \n\n"
pm_caption += "[@WhySooSerious](https://github.com/JyothisJayanth)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete() 
    await borg.send_file(alive.chat_id, PM_GIF,caption=pm_caption)

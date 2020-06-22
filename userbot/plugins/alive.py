"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
PM_IMG = "https://telegra.ph/file/fd2b0fabaae61936f3442.jpg"
pm_caption = "`──────▄▀▄─────▄▀▄ \n─────▄█░░▀▀▀▀▀░░█▄ \n─▄▄──█░░░░░░░░░░░█──▄▄ \n█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█ \nYour bot is running\n\nTelethon version: 6.9.0\nPython: 3.7.3\n\n`"
pm_caption += f"`My Rightful OWNER`: {DEFAULTUSER}\n"
pm_caption += f"`Server HQ` : [Switch SUPERNAP Campus, Las Vegas](www.google.com)\n"
pm_caption += "`Database Status: Databases functioning normally!\n\nAlways with you, MY MASTER!`\n"
pm_caption += "[Deploy this Userbot Now](https://github.com/JyothisJayanth/GujjuBot)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)

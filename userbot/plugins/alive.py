"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`──────▄▀▄─────▄▀▄ \n─────▄█░░▀▀▀▀▀░░█▄ \n─▄▄──█░░░░░░░░░░░█──▄▄ \n█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█ \nYour bot is running\n\nTelethon version: 6.9.0\nPython: 3.7.3\n\n`"
                     f"`My Rightful OWNER`: {DEFAULTUSER}\n"
                     
                     f"`Server HQ` : [Switch SUPERNAP Campus, Las Vegas](https://telegra.ph/file/fd2b0fabaae61936f3442.jpg),\n"
                     "`Database Status: Databases functioning normally!\n\nAlways with you, MY MASTER!`\n".format(media_urls[0], (ms + ms_two)), link_preview=True) 

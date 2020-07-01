"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# thanks to @WhySooSerious 
# thanks to @Sur_vivor  
# final editing by leobrownlee



"""Check if userbot alive or not . 
"""
import os
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, CMD_HELP
from userbot.utils import admin_cmd
from telethon import version
from platform import python_version, uname

ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
if ALIVE_PIC is None:
  ALIVE_GIF = "https://telegra.ph/file/a6c374a64cb906ebdc4d6.mp4"
else:
  ALIVE_GIF = ALIVE_PIC


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"



mod_caption = "**Your Userbot is running**\n\n"
mod_caption += "`SYSTEM STATUS\n\n`"
mod_caption += f"`Python: {python_version()}\n\n`"
mod_caption += f"`Telethon version: {version.__version__}\n`"
mod_caption += "`Server HQ` : [Switch SUPERNAP](https://www.switch.com/about), LA\n`"
mod_caption += "`Database : Amazon Web Services`\n\n``"
mod_caption += "`My Rightful OWNER`: **WRENCH**\n\n"
mod_caption += "`Bot was modified by:` leobrownlee and Sur_vivor\n\n"
mod_caption += "[@WhySooSerious](https://github.com/JyothisJayanth)"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.delete() 
    await borg.send_file(alive.chat_id, ALIVE_GIF,caption=mod_caption)

#By @WhySooSerious,Kangers can Take the Credits 😋
import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from userbot.utils import admin_cmd
import time
 
from userbot import ALIVE_NAME
naam = str(ALIVE_NAME)

bot = "@AniFluidbot"
 
@borg.on(admin_cmd("sanime ?(.*)"))
async def _(event):
    if event.fwd_from:
        return    
    sysarg = event.pattern_match.group(1)
    if sysarg == ""
      async with borg.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/anime" + sysarg)
              result = await conv.get_response()
 
              await borg.send_message(event.chat_id, result.text)
 
              await event.delete()
 

@borg.on(admin_cmd("scharacter ?(.*)"))
 
async def _(event):
 
    if event.fwd_from:
 
        return    
 
    sysarg = event.pattern_match.group(1)
 
    if sysarg == "":
 
      async with borg.conversation(bot) as conv:
 
          try:
 
              await conv.send_message("/start")
 
              response = await conv.get_response()
 
              await conv.send_message("/character" + sysarg)
 
              audio = await conv.get_response()
 
              await borg.send_message(event.chat_id, audio.text)
 
              await event.delete()

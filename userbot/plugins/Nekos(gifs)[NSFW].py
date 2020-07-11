#Serious Kangers can take the Credits xD, by @WhySooSerious
#From Nekos API
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd

@borg.on(admin_cmd("sologif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Solo GIF..```\n**It's Barely SFW**")
    async with borg.conversation(chat) as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
              await borg.send_message(chat, "/sologif")
              response = await response
          except YouBlockedUserError:
              await event.reply("```Please unblock @KeikoSDbot and try again```")
              return
          if response.text.startswith("Forward"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
          else:
             await borg.send_file(event.chat_id, response.message.media)

@borg.on(admin_cmd("cumgif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Henti Cum GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
              await borg.send_message(chat, "/cumgif")
              response = await response
          except YouBlockedUserError:
              await event.reply("```Please unblock @KeikoSDbot and try again```")
              return
          if response.text.startswith("Forward"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
          else:
             await borg.send_file(event.chat_id, response.message.media)

@borg.on(admin_cmd("ngif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Neko GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
              await borg.send_message(chat, "/ngif")
              response = await response
          except YouBlockedUserError:
              await event.reply("```Please unblock @KeikoSDbot and try again```")
              return
          if response.text.startswith("Forward"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
          else:
             await borg.send_file(event.chat_id, response.message.media)

@borg.on(admin_cmd("tickle"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Tickle GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
              await borg.send_message(chat, "/tickle")
              response = await response
          except YouBlockedUserError:
              await event.reply("```Please unblock @KeikoSDbot and try again```")
              return
          if response.text.startswith("Forward"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
          else:
             await borg.send_file(event.chat_id, response.message.media)

@borg.on(admin_cmd("feed"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Feeding GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
              await borg.send_message(chat, "/feed")
              response = await response
          except YouBlockedUserError:
              await event.reply("```Please unblock @KeikoSDbot and try again```")
              return
          if response.text.startswith("Forward"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
          else:
             await borg.send_file(event.chat_id, response.message.media)

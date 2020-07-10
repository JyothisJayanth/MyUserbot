"""
Get information about anime, manga or characters from [MyAnimeList](https://myanimelist.net).
──「 **Anime** 」──
-> `sanime <anime>`
returns information about the anime.
__Original Module by @Zero_cooll7870__
──「 **Character** 」──
-> `scharacter <character>`
returns information about the character.
──「 **Manga** 」──
-> `manga <manga>`
returns information about the manga.
──「 **Upcoming Anime** 」──
-> `upcoming`
returns a list of new anime in the upcoming seasons.
"""
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="anime ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    chat = "@AniFluidbot"
    await event.edit("```Fetching Anime Details...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=778490365))
              await event.client.send_message(chat, "/anime{}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Master! Please Unblock (@AniFluidbot) ```")
              return
          if response.text.startswith("Not Found!"):
             await event.edit("😶**Anime Not Found**😅\n\n[Contact @WhySooSerious for more info..](https://t.me/WhySooSerious)")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)

@borg.on(admin_cmd(pattern="character ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    chat = "@AniFluidbot"
    await event.edit("```Fetching Character Details...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=778490365))
              await event.client.send_message(chat, "/character {}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Master! Please Unblock (@AniFluidbot) ```")
              return
          if response.text.startswith("Not Found!"):
             await event.edit("😶**Anime Not Found**😅\n\n[Contact @WhySooSerious for more info..](https://t.me/WhySooSerious)")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)

################################


@borg.on(admin_cmd(pattern="sanime ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    chat = "@NepgearBot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1072580256))
              await event.client.send_message(chat, "/anime {}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Master! Please Unblock (@NepgearBot) ```")
              return
          if response.text.startswith("Country"):
             await event.edit("**Fetching Details..**")
          else: 
             await event.delete()
             response = await response
             await event.client.send_message(event.chat_id, response.message)

#####################################


@borg.on(admin_cmd(pattern="covid ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    chat = "@NovelCoronaBot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1124136160))
              await event.client.send_message(chat, "{}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Master! Please Unblock (@NovelCoronaBot) ```")
              return
          if response.text.startswith("Country"):
             await event.edit("😶**Country Not Found**😅\n\n[🔴🔴🔴🔴\n ⏩⏩ How to use ⏪⏪\n🔵🔵🔵🔵](https://t.me/Dev_OwO)")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)

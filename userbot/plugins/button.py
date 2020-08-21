# Test Plugin for Inline Buttons by @WhySooSerious
from userbot  import STRING_SESSION, APP_ID, API_HASH, BOT_TOKEN
from telethon import TelegramClient, Button, events 
from userbot.utils import admin_cmd

if STRING_SESSION:
    # pylint: disable=invalid-name
    bot = TelegramClient(StringSession(STRING_SESSION), APP_ID, API_HASH)
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("userbot", APP_ID, API_HASH)

with bot:
    try:
        tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=APP_ID,
            api_hash=API_HASH).start(
            bot_token=BOT_TOKEN)

@borg.on(admin_cmd(pattern="butt"))
async def butt(event):

    keyboard = [
        [  
            Button.inline("First option", b"1"), 
            Button.inline("Second option", b"2")
        ],
        [
            Button.inline("Third option", b"3"), 
            Button.inline("Fourth option", b"4")
        ],
        [
            Button.inline("Fifth option", b"5")
        ]
    ]

    await tgbot.send_message(event.chat_id, "Choose an option:", buttons=keyboard)
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from userbot import bot
from userbot.utils import load_module, start_assistant
from userbot import TGBOT_USERNAME, TGBOT_TOKEN, API_HASH, APP_ID


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if TGBOT_USERNAME is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=APP_ID, api_hash=API_HASH
        ).start(bot_token=TGBOT_TOKEN)
        print("Initialisation finished with no errors")
        print("Starting To Install Inline In Bot")
        bot.loop.run_until_complete(add_bot(TGBOT_USERNAME))
        print("Startup Completed")
    else:
        bot.start()


import glob
path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))
# Done.
path = "userbot/plugins/assistant/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_assistant(shortname.replace(".py", ""))

print("Userbot And Assistant Bot Have Been Installed Successfully !")
print("Enjoy!")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
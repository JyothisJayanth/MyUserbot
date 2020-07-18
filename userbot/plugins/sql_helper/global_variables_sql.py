# global variables will be assigned here
# can be imported in any module to make life easier.
from userbot.uniborgConfig import Config
import asyncio
from telethon.tl.types import ChannelParticipantsAdmins
	
GN = "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･\n╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮\n╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫\n┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯\n╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥° ♥｡･ﾟ♡ﾟ･"
GM = "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･\n╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮\n╭━┳━┳━┳╯┃╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n┣╮┣━┻━┻━╯╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･"
LIKE = "👍🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👇🏿👍🏿\n👉🏿👍🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👇🏾👍🏾👈🏿\n👉🏿👉🏾👍🏽👇🏽👇🏽👇🏽👇🏽👇🏽👍🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👍🏼👇🏼👇🏼👇🏼👍🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👉🏼👍🏻👇🏻👍🏻👈🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👉🏼👉🏻❤👈🏻👈🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👉🏼👍🏻👆🏻👍🏻👈🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👉🏽👍🏼👆🏼👆🏼👆🏼👍🏼👈🏽👈🏾👈🏿\n👉🏿👉🏾👍🏽👆🏽👆🏽👆🏽👆🏽👆🏽👍🏽👈🏾👈🏿\n👉🏿👍🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👆🏾👍🏾👈🏿\n👍🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👆🏿👍🏿"
LOL = "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥•°\n╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ \n╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ \n╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ \n╱┗━━━┛╰━━━╯┗━━━┛╱\n｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥°•"


LOGGER = Config.PRIVATE_GROUP_BOT_API_ID
BLACKLIST = Config.UB_BLACK_LIST_CHAT
SYNTAX = {}
SUDO_USERS = Config.SUDO_USERS
COUNT_MSG = 0
USERS = {}
COUNT_PM = {}
LASTMSG = {}
CMD_HELP = {}
ISAFK = False
AFKREASON = None
BUILD = "Plus+"
MODULE = []

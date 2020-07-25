#autobio for @WhySooSerious, Edit bio strings Amigo if u use this plugin, Or else u are cursed :)
import asyncio
import time
from telethon.tl import functions
from telethon.errors import FloodWaitError
from userbot.utils import admin_cmd
from userbot import CMD_HELP


DEL_TIME_OUT = 60


@borg.on(admin_cmd(pattern="bio"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d/%m/%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"No PMs ¦ Too Lazy to Write a Bio // @TeamCyphers // 📅 ({DMY})"
        logger.info(bio)
        try:
            await borg(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                about=bio
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
            # logger.info(r.stringify())
            # await borg.send_message(  # pylint:disable=E0602
            #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
            #     "Successfully Changed Profile Bio"
            # )
        await asyncio.sleep(DEL_TIME_OUT)

CMD_HELP.update({
    'bio': ".bio\
    \nUsage: This Plugin is Exclusively for @WhySooSerious."
})
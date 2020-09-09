"""Userbot help command"""

from userbot import CMD_HELP
from userbot.events import register


@borg.on(admin_cmd(pattern="chelp(?: |$)(.*)"))
@borg.on(sudo_cmd(pattern="chelp(?: |$)(.*),allow_sudo=True))
async def help(event):
    """For .chelp command"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("Please specify a valid module name.")
    else:
        string = "Specify which module do you want help for !!\n**Usage:** `.chelp` <module name>\n\n"
        for i in sorted(CMD_HELP):
            string += "`" + str(i) + "`"
            string += "\t\t\t||\t\t\t "
        await event.edit(string)
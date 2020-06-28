import logging
import requests
import asyncio

from .. import loader, utils

logger = logging.getLogger(__name__)


def sgen(agen, loop):
    while True:
        try:
            yield utils.run_async(loop, agen.__anext__())
        except StopAsyncIteration:
            return


@loader.tds
class TransferShMod(loader.Module):
    """Upload to and from transfer.sh"""
    strings = {"name": "transfer.sh support",
               "up_cfg_doc": "URL to upload the file to.",
               "no_file": "<code>Provide a file to upload</code>",
               "uploading": "<code>Uploading...</code>",
               "uploaded": "<a href={}>Uploaded!</a>"}

    def __init__(self):
        self.config = loader.ModuleConfig("UPLOAD_URL", "https://transfer.sh/{}",
                                          lambda m: self.strings("up_cfg_doc", m))

    @loader.unrestricted
    @loader.ratelimit
    async def uploadshcmd(self, message):
        """Uploads to transfer.sh"""
        if message.file:
            msg = message
        else:
            msg = (await message.get_reply_message())
        doc = getattr(msg, "media", None)
        if doc is None:
            await utils.answer(message, self.strings("no_file", message))
            return
        doc = message.client.iter_download(doc)
        logger.debug("begin transfer")
        await utils.answer(message, self.strings("uploading", message))
        r = await utils.run_sync(requests.put, self.config["UPLOAD_URL"].format(msg.file.name),
                                 data=sgen(doc, asyncio.get_event_loop()))
        logger.debug(r)
        r.raise_for_status()
        logger.debug(r.headers)
        await utils.answer(message, self.strings("uploaded", message).format(r.text))

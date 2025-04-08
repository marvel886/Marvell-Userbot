from telethon import Button
from AyiinXd import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    STRING_SESSION,
    blacklistayiin,
    bot,
    tgbot,
)

async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://graph.org/file/e440505e4a8d6a41fb1c6-9fe6780cac5039ecbc.jpg",
                caption="𝗠𝗮𝗿𝘃𝗲𝗹𝗹-𝗨𝘀𝗲𝗿𝗯𝗼𝘁.\n     **status : Active\n     ketik `.ping` untuk cek bot!**",
                buttons=[(Button.url("Store", "https://t.me/jasebmarvell")),
                         (Button.url("Support", "https://t.me/marvellcs"))]
            )
    except Exception as e:
        LOGS.error(e)
        return None

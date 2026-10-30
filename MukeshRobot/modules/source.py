from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from MukeshRobot import START_IMG, dispatcher, pbot


@pbot.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""**ʜᴇʏ {message.from_user.mention()}!**

ɪ ᴀᴍ [{dispatcher.bot.first_name}](https://t.me/{dispatcher.bot.username}), ᴀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ.

**» ᴍᴀɪɴᴛᴀɪɴᴇʀ:** [TP Editz](https://github.com/tpeditz)
**» sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ:** [BestManagementbot](https://github.com/tpeditz/BestManagementbot)

**» ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ:** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ:** `{o}`
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ:** `{s}`
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ:** `{z}`

ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ TP EDITZ.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• TP EDITZ •", url="https://github.com/tpeditz"),
                    InlineKeyboardButton(
                        "• SOURCE •",
                        url="https://github.com/tpeditz/BestManagementbot",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"
__help__ = """
/repo  - ᴠɪᴇᴡ ᴛʜᴇ ʀᴇᴘᴏsɪᴛᴏʀʏ ᴀɴᴅ ʙᴏᴛ ɪɴғᴏ
/source - ᴠɪᴇᴡ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ
"""

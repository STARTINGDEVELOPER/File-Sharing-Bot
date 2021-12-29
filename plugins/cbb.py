#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>➠ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n➠ Language : <code>Python3</code>\n➠ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n➠ Channel : <a href='https://t.me/CINEMAGROUPOFFICIAL'>Cɪɴᴇᴍᴀ Gʀᴏᴜᴘ Oꜰꜰɪᴄɪᴀʟ​</a>\n➠ Group : <a href='https://t.me/+jJsgcK780oVmNTM9'>𝐂𝐈𝐍𝐄𝐌𝐀 𝐆𝐑𝐎𝐔𝐏 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋​</a>\n,
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

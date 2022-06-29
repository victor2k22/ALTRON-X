from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram import Client, filters
from __main__ import *
 
 
ALIVE_PIC = "https://te.legra.ph/file/0957630b8248e79400247.jpg"

 
@Client.on_message(filters.command(["help"], [".", "/", "!"]) & filters.me)
async def alive(client: Client, e: Message):
    ids = 0
    try:
        if client:
            ids += 1
        if client1:
            ids += 1
        if client2:
            ids += 1
        if client3:
            ids += 1
        if client4:
            ids += 1
        if client5:
            ids += 1
        if client6:
            ids += 1
        if client7:
            ids += 1
        if client8:
            ids += 1
        if client9:
            ids += 1
        Alive_msg = f"𝐀𝐥𝐭𝐫𝐨𝐧 𝐈𝐬 𝐎𝐧 𝐅𝐢𝐫𝐞 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► Vᴇʀsɪᴏɴ : `1.0` \n"
        Alive_msg += f"► Pʏʀᴏ ᴠᴇʀsɪᴏɴ : `1.4.16` \n"
        Alive_msg += f"► Aᴄᴛɪᴠᴇ IDs : `{ids}` \n"
        Alive_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ.](t.me/TheAltron) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 •", url="https://t.me/Superior_Bots")
                ], [
                    InlineKeyboardButton(
                        "• 𝐑𝐞𝐩𝐨 •", url="https://github.com/ITZ-ZAID/ZAID-USERBOT")
                ]],
        ),
    ) 
    except Exception as lol:         
        Alive_msg = f"𝐀𝐥𝐭𝐫𝐨𝐧 𝐈𝐬 𝐎𝐧 𝐅𝐢𝐫𝐞 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► Vᴇʀsɪᴏɴ : `1.0` \n"
        Alive_msg += f"► Pʏʀᴏ ᴠᴇʀsɪᴏɴ : `1.4.16` \n"
        Alive_msg += f"► Sᴜᴘᴘᴏʀᴛ : [Jᴏɪɴ](t.me/TheAltron) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 •", url="https://t.me/Superior_Bots"),
                ],
                [
                    InlineKeyboardButton("• 𝐑𝐞𝐩𝐨 •", url="https://github.com/Itz-Zaid/Zaid-Userbot"),
                ],
            ],
        ),
    ) 



from pyrogram import filters, Client
from pyrogram.types import Message
from modules.__main__ import *
from config import SUDO_USERS


ALIVE_PIC = "https://te.legra.ph/file/0957630b8248e79400247.jpg"
 
 
@Client.on_message(filters.command(["alive", "awake"], [".", "/", "!"]) & filters.user(SUDO_USERS))
@Client.on_message(filters.command(["alive", "awake"], [".", "/", "!"]) & filters.me)
async def alive(Client, e: Message):
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
        Alive_msg = f"Aʟᴛʀᴏɴ Is Oɴ Fɪʀᴇ 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► Vᴇʀsɪᴏɴ : `1.0` \n"
        Alive_msg += f"► Pʏʀᴏ ᴠᴇʀsɪᴏɴ : `1.4.16` \n"
        Alive_msg += f"► Aᴄᴛɪᴠᴇ IDs : `{ids}` \n"
        Alive_msg += f"► Uᴘᴅᴀᴛᴇs : [Aʟᴛʀᴏɴ X](t.me/Altron_X)\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg
    ) 
    except Exception as lol:         
        Alive_msg = f"Aʟᴛʀᴏɴ Is Oɴ Fɪʀᴇ 🔥 \n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► Vᴇʀsɪᴏɴ : `1.0` \n"
        Alive_msg += f"► Pʏʀᴏ ᴠᴇʀsɪᴏɴ : `1.4.16` \n"
        Alive_msg += f"► Aᴄᴛɪᴠᴇ IDs : `{ids}` \n"
        Alive_msg += f"► Uᴘᴅᴀᴛᴇs : [Aʟᴛʀᴏɴ X](t.me/Altron_X)\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply(Alive_msg) 

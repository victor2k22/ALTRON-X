import asyncio
from pyrogram import Client
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from modules.helpers.command import commandpro
from config import SUDO_USERS

@Client.on_message(commandpro(["/gcast", "/cast", "!gcast", "!cast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("**`Sᴛᴀʀᴛɪɴɢ Gᴄᴀsᴛ Fʀᴏᴍ Aʟʟ IDs ...`**")
        if not message.reply_to_message:
            await wtf.edit("**Pʟᴇᴀsᴇ Rᴇᴘʟʏ Tᴏ A Mᴇssᴀɢᴇ ...**")
            return
        lmao = message.reply_to_message.text
        async for dialog in Client.iter_dialogs():
            try:
                await Client.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"**🌹 𝐁𝐫𝐨𝐚𝐝𝐜𝐚𝐬𝐭𝐢𝐧𝐠 ...** \n\n**✅ Sᴇɴᴛ:** `{sent}` \n**❌ Fᴀɪʟᴇᴅ:** `{failed}` ")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await wtf.delete()
        await message.reply_text(f"**🌷 𝐆𝐜𝐚𝐬𝐭 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ...**\n\n**✅ Sᴇɴᴛ Tᴏ:** `{sent}` **Cʜᴀᴛs**\n**❌ Fᴀɪʟᴇᴅ Iɴ:** `{failed}` **Cʜᴀᴛs**")

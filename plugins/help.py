import asyncio
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS

@Client.on_message(commandpro(["!help", "/help", ".help"]) & filters.me)
@Client.on_message(commandpro(["!help", "/help", ".help"]) & filters.user(SUDO_USERS))
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/0957630b8248e79400247.jpg",
        caption=f"""**
★<𝐀𝐋𝐓𝐑𝐎𝐍 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒>★

┏━━━━━━━━━━━━━━━━━┓ 
┣★P - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴇɴᴊᴏʏ ᴍᴜsɪᴄ
┣★E - ᴛᴏ ᴇɴᴅ sᴏɴɢ
┣★!skip - ᴛᴏ sᴋɪᴘ sᴏɴɢ
┣★!pause - ᴛᴏ ᴘᴀᴜsᴇ ʀᴜɴɴɪɴɢ sᴏɴɢ 
┣★!resume - ᴛᴏ ʀᴇsᴜᴍᴇ ᴘᴀᴜsᴇᴅ sᴏɴɢ
┣★!fspam - ғᴏʀ ғᴀsᴛ sᴘᴀᴍ
┣★!spam - ғᴏʀ sᴘᴀᴍ
┣★!delspam - ᴀғᴛᴇʀ sᴘᴀᴍ ᴍsɢ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ
┣★!dspam - ғᴏʀ sʟᴏᴡ sᴘᴀᴍ
┣★!sspam - ғᴏʀ sᴛɪᴄᴋᴇʀ sᴘᴀᴍ
┣★!join [ɪɴᴠɪᴛᴇ ʟɪɴᴋ] - ᴛᴏ ᴊᴏɪɴ ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ 
┣★!join [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ] - ᴛᴏ ᴊᴏɪɴ ᴘᴜʙʟɪᴄ ɢʀᴏᴜᴘ
┣★!leave [ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ] - ғᴏʀ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ
┣★!leave [ɪɴᴠɪᴛᴇ ʟɪɴᴋ] - ғᴏʀ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ
┣★!inviteall- ᴛᴏ ᴀᴅᴅ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜᴀᴛ ɢʀᴏᴜᴘ ᴡʜᴇʀᴇ ᴛʜᴇ ᴄᴍᴅ ɪs ᴇxᴇᴄᴜᴛᴇᴅ
┣★!raid [QUANTITY] - ᴛᴏ ʀᴀɪᴅ ᴏɴ ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ
┣★!dmraid [QUANTITY] - ᴛᴏ ʀᴀɪᴅ ᴏɴ ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ ɪɴ ᴅᴍ        
┣★!clean - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴊᴜɴᴋ ғɪʟᴇs
┣★!alive - ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ
┣★!help - ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴍsɢ
┗━━━━━━━━━━━━━━━━━┛**""")



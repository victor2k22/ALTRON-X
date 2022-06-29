from pyrogram import Client as bot, filters
from modules.helpers.command import commandpro
from modules.helpers.decorators import errors, sudo_users_only
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@bot.on_message(commandpro(["/help", "!help", ".help"]))
@bot.on_message(commandpro(["/help", "!help", ".help"]) & filters.me)
@errors
@sudo_users_only
def help_(bot, message):
    HELP_TXT = """
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
┗━━━━━━━━━━━━━━━━━┛
"""
    
    message.reply_photo(
        photo="https://te.legra.ph/file/0957630b8248e79400247.jpg",
        caption=HELP_TXT
    )

     
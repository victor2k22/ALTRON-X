from pyrogram import Client as bot, filters
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@bot.on_message(filters.command("help"))
def help_(bot, message):
    HELP_TXT = """Hoi \nHere is the help menu choose your desireoption nd explorer it!!\nFor any kind of help or query Just join @Altron_X and ask your query!!"""
    
    HELP_BUTTON = [
        [
            InlineKeyboardButton(text="ᴠᴄ", callback_data="vc"),
            InlineKeyboardButton(text="sᴘᴀᴍ", callback_data="spam"),
            InlineKeyboardButton(text="ɪɴᴠɪᴛᴇ", callback_data="admin_cmd"),
        ],
        [
            InlineKeyboardButton(text="ʀᴀɪᴅ", callback_data="raid"), 
            InlineKeyboardButton(text="ᴀᴅᴠᴀɴᴄᴇ", callback_data="advance"), 
        ],   
        [
            InlineKeyboardButton(text="ᴄʟᴏsᴇ 🗑", callback_data="close"),
        ],
    ]
    message.reply_photo(
        photo="https://te.legra.ph/file/0957630b8248e79400247.jpg",
        caption=HELP_TXT,
        reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
    )
    message.delete()

@bot.on_callback_query()
def callback_query(Client, callback: CallbackQuery):
    if callback.data == "help_":
    
        HELP_TXT = f"""Hoi, Here is the help menu choose your desireoption nd explorer it!!\nFor any kind of help or query Just join @Altron_X and ask your query!!"""
    
        HELP_BUTTON = [
        [
            InlineKeyboardButton(text="ᴠᴄ", callback_data="vc"),
            InlineKeyboardButton(text="sᴘᴀᴍ", callback_data="spam"),
            InlineKeyboardButton(text="ɪɴᴠɪᴛᴇ", callback_data="admin_cmd"),
        ],
        [
            InlineKeyboardButton(text="ʀᴀɪᴅ", callback_data="raid"),
            InlineKeyboardButton(text="ᴀᴅᴠᴀɴᴄᴇ", callback_data="advance"), 
        ],   
        [
            InlineKeyboardButton(text="ᴄʟᴏsᴇ 🗑", callback_data="close"),
        ],
    ]
        callback.edit_message_text(
            HELP_TXT,
            reply_markup=InlineKeyboardMarkup(HELP_BUTTON)
        )
    elif callback.data == "vc":
        B_HELP = """
P - use this command and enjoy music
E - To End Song
Skip - To Skip Song
Pause - To pause running song 
Resume - To Resume paused song
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="Close", callback_data="close"),
                InlineKeyboardButton(text="Back", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            B_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "spam":
        SPM_HELP = """
!fspam - For fast spam
!spam - for spam
!delspam - after spam msg will be deleted
!dspam - For Slow spam
!sspam - For Sticker Spam
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="Close", callback_data="close"),
                InlineKeyboardButton(text="Back", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            SPM_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "admin_cmd":
        A_HELP = """
!join [INVITE LINK] - TO join private group 
!join [GROUP USERNAME] - TO JOIN PUBLIC GROUP
!leave [GROUP USERNAME] - FOR leave group
!leave [INVITE LINK] - FOR LEAVE GROUP

!inviteall- To Add members in that group where the cmd is executed
"""
        BUTTON = [
            [
                InlineKeyboardButton(text="Close", callback_data="close"),
                InlineKeyboardButton(text="Back", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            A_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )
    elif callback.data == "raid":
        C_HELP = """
!raid [QUANTITY] - TO RAID ON REPLIED USER
!dmraid [QUANTITY] - TO RAID ON REPLIED USER IN DM 
!rraid - SOON ADDING THIS..... 

"""
        BUTTON = [
            [
                InlineKeyboardButton(text="Close", callback_data="close"),
                InlineKeyboardButton(text="Back", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            C_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )        
    elif callback.data == "advance":
        D_HELP = """
/clean - To delete junk files
/alive - To check bot is alive or dead
/help - to get help msg
/song - to download song
/video to download video

"""
        BUTTON = [
            [
                InlineKeyboardButton(text="Close", callback_data="close"),
                InlineKeyboardButton(text="Back", callback_data="help_"),
            ],
        ]
        callback.edit_message_text(
            D_HELP,
            reply_markup=InlineKeyboardMarkup(BUTTON)
        )        
    elif callback.data == "close":
        callback.message.delete()
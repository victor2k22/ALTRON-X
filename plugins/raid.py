from pyrogram.types import *
import os
import sys
import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from modules.data import *
from config import *


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], [".", "/", "!"]))
@Client.on_message(filters.me & filters.command(["raid"], [".", "/", "!"]))
async def dmraid(xspam: Client, e: Message):
      """ Module: Raid """
      TheAltronX = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = e.chat.id
          if int(id) in VERIFIED_USERS:
                text = f"Chal Chal baap Ko mat sikha"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"Abe Lawde that guy part of my devs."
                await e.reply_text(text)
          else:
              counts = int(TheAltronX[0])
              await e.reply_text("Raid Strated Successfully")
              for _ in range(counts):
                    reply = choice(RAID)
                    msg = f"[{ok.first_name}](tg://user?id={ok.id}) {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(3)


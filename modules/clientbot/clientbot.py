import requests
import os
import logging
from pyrogram import Client as Bot
from pyrogram.types import *
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream
from config import API_ID, API_HASH, STRING_SESSION, STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4, STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8, STRING_SESSION9
from . import queues

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


if STRING_SESSION:
    client = Bot(STRING_SESSION, API_ID, API_HASH, plugins=dict(root="plugins"))
else:
    client = None    

if STRING_SESSION1:
    client1 = Bot(STRING_SESSION1, API_ID, API_HASH, plugins=dict(root="plugins"))
else:
    client1 = None

if STRING_SESSION2:
    client2 = Bot(STRING_SESSION2, API_ID, API_HASH, plugins=dict(root="plugins"))
else:
    client2 = None

if STRING_SESSION3:
    client3 = Bot(STRING_SESSION3, API_ID, API_HASH, plugins=dict(root="plugins"))
else:
    client3 = None

if STRING_SESSION4:
    client4 = Bot(STRING_SESSION4, API_ID, API_HASH, plugins=dict(root="plugins"))
else:
    client4 = None

if STRING_SESSION5:
    client5 = Bot(STRING_SESSION5, API_ID, API_HASH, plugins=dict(root="plugins"))
else:
    client5 = None

if STRING_SESSION6:
    client6 = Bot(STRING_SESSION6, API_ID, API_HASH, plugins=dict(root="plugins"))
else:
    client6 = None

if STRING_SESSION7:
    client7 = Bot(STRING_SESSION7, API_ID, API_HASH, plugins=dict(root="plugins"))
else:
    client7 = None

if STRING_SESSION8:
    client8 = Bot(STRING_SESSION8, API_ID, API_HASH, plugins=dict(root="plugins"))
else:
    client8 = None

if STRING_SESSION9:
    client9 = Bot(STRING_SESSION9, API_ID, API_HASH, plugins=dict(root="plugins"))
else:
    client9 = None


pytgcalls = PyTgCalls(client)


@pytgcalls.on_stream_end()
async def on_stream_end(client: PyTgCalls, update: Update) -> None:
    chat_id = update.chat_id
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        await pytgcalls.leave_group_call(chat_id)
    else:
        await pytgcalls.change_stream(
            chat_id, 
            InputStream(
                InputAudioStream(
                    queues.get(chat_id)["file"],
                ),
            ),
        )



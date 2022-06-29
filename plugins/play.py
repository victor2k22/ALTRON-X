import os
import aiofiles
import aiohttp
import ffmpeg
import requests
from os import path
from asyncio.queues import QueueEmpty
from typing import Callable
from pyrogram import filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from modules.cache.admins import set
from modules.clientbot import clientbot, queues
from modules.clientbot.clientbot import client as USER
from modules.helpers.admins import get_administrators
from youtube_search import YoutubeSearch
from modules import converter
from modules.downloaders import youtube
from config import que, SUDO_USERS
from modules.cache.admins import admins as a
from modules.helpers.command import commandpro
from modules.helpers.filters import command, other_filters
from modules.helpers.decorators import errors, sudo_users_only
from modules.helpers.errors import DurationLimitError
from modules.helpers.gets import get_url, get_file_name
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream

# plus
chat_id = None
useer = "NaN"


def transcode(filename):
    ffmpeg.input(filename).output(
        "input.raw", format="s16le", acodec="pcm_s16le", ac=2, ar="48k"
    ).overwrite_output().run()
    os.remove(filename)


# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))



@USER.on_message(
    commandpro(["p", "play", "/play", "@", "ply"])
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
@errors
@sudo_users_only
async def play(_, message: Message):
    global que
    global useer
    await message.delete()
    lel = await message.reply("**🔄 Ƥɤøƈɘssɩɳʛ...**")

    administrators = await get_administrators(message.chat)
    chid = message.chat.id


    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://telegra.ph/file/0f6f8a8a5ad69fe5ecf3d.png"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Locally added"


        requested_by = message.from_user.first_name
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

            
        except Exception as e:
            title = "NaN"
            thumb_name = "https://telegra.ph/file/0f6f8a8a5ad69fe5ecf3d.png"
            duration = "NaN"
            views = "NaN"

        requested_by = message.from_user.first_name
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
           return await lel.edit(
                "**🤖 Wɦɑʈ 🙃 Yøʋ 💿 Wɑŋʈ 😍\n💞 Ƭø 🔊 Ƥɭɑy❓ ...**"
            )

        await lel.edit("**🔎 Sɘɑɤƈɦɩɳʛ ...**")
        query = message.text.split(None, 1)[1]
        # print(query)
        await lel.edit("**🔄 Ƥɤøƈɘssɩɳʛ ...**")
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await lel.edit(
                "**🔊 Ɱʋsɩƈ 😕 Ɲøʈ 📵 Føʋɳɗ❗️\n💞 Ƭɤy ♨️ Ʌɳøʈɦɘɤ 🌷...**"
            )
            print(str(e))
            return


        requested_by = message.from_user.first_name
        file_path = await converter.convert(youtube.download(url))
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)
        await lel.edit("**💥 Ʌɗɗɘɗ 💿 Søɳʛ❗️\n🔊 Ʌʈ 💞 Ƥøsɩʈɩøɳ » `{}` 🌷 ...**".format(position),
    )
    else:
        await clientbot.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )

        await lel.edit("**💥 Mʋsɩƈ 🎸 Nøω 💞\n🔊 Ƥɭɑyɩɳʛ 😍 ØƤ 🥀 ...**".format(),
        )

    return await lel.delete()
    
    
    
@USER.on_message(commandpro(["Pause", "/pause", ".pause", "!pause", "pse"]) & other_filters)
@errors
@sudo_users_only
async def pause(_, message: Message):
    await message.delete()
    await clientbot.pytgcalls.pause_stream(message.chat.id)
    pase = await message.reply_text("**▶️ Ƥɑʋsɘɗ 🌷...**")
    await pase.delete()

@USER.on_message(commandpro(["Resume", "/resume", "!resume", ".resume", "rsm"]) & other_filters)
@errors
@sudo_users_only
async def resume(_, message: Message):
    await message.delete()
    await clientbot.pytgcalls.resume_stream(message.chat.id)
    rsum = await message.reply_text("**⏸ Ʀɘsʋɱɘɗ 🌷...**")
    await rsum.delete()


@USER.on_message(commandpro(["Skip", "/skip", ".resume", "!skip", "/next", "skp", "nxt"]) & other_filters)
@errors
@sudo_users_only
async def skip(_, message: Message):
    global que
    await message.delete()
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
       novc = await message.reply_text("**💥 Ɲøʈɦɩɳʛ 🔇 Ƥɭɑyɩɳʛ 🌷...**")
       await novc.delete()
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            empt = await message.reply_text("**🥀 Nøʈɦɩɳʛ 💫 ʈø 💥 ɭɘɑⱱɩɳʛ ⚡ VC ✨...**")
            await empt.delete()
            await clientbot.pytgcalls.leave_group_call(chat_id)
        else:
            next = await message.reply_text("**⏩ Sƙɩƥƥɘɗ 🌷...**")
            await next.delete()
            await clientbot.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        clientbot.queues.get(chat_id)["file"],
                    ),
                ),
            )
             


@USER.on_message(commandpro(["/end", "/stop", "E", "S", "end", "stp"]) & other_filters)
@errors
@sudo_users_only
async def stop(_, message: Message):
    await message.delete()
    try:
        clientbot.queues.clear(message.chat.id)
    except QueueEmpty:
        pass

    await clientbot.pytgcalls.leave_group_call(message.chat.id)
    leav = await message.reply_text("**❌ Sʈøƥƥɘɗ 🌷...**")
    await leav.delete()

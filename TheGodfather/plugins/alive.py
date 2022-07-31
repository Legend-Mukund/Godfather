from config import PREFIX
import asyncio
import time
from datetime import datetime
from pyrogram import filters, Client
from TheGodfather import StartTime, CMD_HELP
from sys import version_info

from pyrogram import __version__ as __pyro_version__
from pyrogram.types import Message

CMD_HELP.update(
    {
        "Alive": """
『 **Alive** 』
  `alive` -> Show off to people with your bot using this command.
  `ping` -> Shows you the response speed of the bot.
"""
    }
)

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@Client.on_message(filters.command("alive", PREFIX) & filters.me)
async def alive(app: Client, m):
    start_time = time.time()
    uptime = get_readable_time((time.time() - StartTime))
    end_time = time.time()
    reply_msg = f"**★彡[ʜᴇʏ! ɪ'ᴍ ꜱᴛɪʟʟ ᴀᴡᴀᴋᴇ!]彡★**\n"
    reply_msg += f"📂 ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ: `{__python_version__}`\n"
    reply_msg += f"📂 ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ: `{__pyro_version__}`\n"
    reply_msg += f"📂 ᴜᴘᴛɪᴍᴇ: {uptime}"
    reply_msg += "\n📂 ꜱᴜᴘᴘᴏʀᴛ: [Click](https://t.me/TheGodfatherChat)\n📂 ᴄʜᴀɴɴᴇʟ: [Click](https://t.me/GodfatherUserBot)\n\n[**★彡[ᴘᴏᴡᴇʀᴇᴅ ʙʏ ɢᴏᴅꜰᴀᴛʜᴇʀ]彡★**](https://github.com/Team-TGN/Godfather)"
    photo = "https://telegra.ph/file/2c564b0cd45f8e39ef7e2.jpg"
    await m.delete()
    if m.reply_to_message:
        await app.send_photo(
            m.chat.id,
            photo,
            caption=reply_msg,
            reply_to_message_id=m.reply_to_message.message_id,
        )
    else:
        await app.send_photo(m.chat.id, photo, caption=reply_msg)


start = time.time()
end = time.time()
ping = round((end - start) * 1000, 3)
uptime = get_readable_time((time.time() - StartTime))

if ping <= 100:
    pingx = "🎒 sᴍᴏᴏᴛʜ ᴀғ ~"
if ping <= 200:
    pingx = '🎒 ғɪɴᴇ ᴀғ ~'
if ping <= 300:
    pingx = '🎒 ᴀᴠᴇʀᴀɢᴇ ᴀғ ~'
if ping <= 400:
    pingx = '🎒 sʟᴏᴡ ᴀғ ~' 
if ping >= 500:
    pingx = '⚠ ᴄʜᴇᴄᴋ ʏᴏᴜ ɴᴇᴛᴡᴏʀᴋ ᴄᴏɴɴᴇᴄᴛɪᴏɴ'

@Client.on_message(filters.command("ping", PREFIX) & filters.me)
async def alive(app: Client, m):
    await m.delete()
    asyncio.sleep(0.5)
    await m.send_photo(
        m.chat.id,
        photo = "https://telegra.ph/file/2c564b0cd45f8e39ef7e2.jpg",
        caption = f"""
ᴘᴏɴɢ 🍁

ᴛɪᴍᴇ ᴛᴏᴏᴋ : `{ping}`

ᴜᴘᴛɪᴍᴇ : `{uptime}`

ᴄᴏɴᴅɪᴛɪᴏɴ : **{pingx}**

ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `{p}`

ɢᴏᴅғᴀᴛʜᴇʀ ᴠᴇʀsɪᴏɴ : `{__meta__}`
"""
    )


__MODULE__ = "Alive"
__HELP__ = f"""
**📂 To Check Alive Message.**
`.alive` - **To check alive**
`.ping` - **To Check bot Uptime**
"""


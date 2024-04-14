from requests import get
from pyrogram import filters
from pyrogram.types import Message
from DAXXMUSIC import app

@app.on_message(filters.command("slap"))
async def es_url(_, message):
    try:
        api = "https://api.otakugifs.xyz/gif?reaction=slap&format=gif"
        get_slap = get(api)
        get_json = get_slap.json()
        get_gif_url = get_json["url"]
        await message.reply_video(get_gif_url)
    except:
        pass

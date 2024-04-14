from requests import get
from pyrogram import filters
from pyrogram.types import Message
from DAXXMUSIC import app

@app.on_message(filters.command("bite"))
async def es_url(_, message):
    try:
        api = "https://api.waifu.pics/sfw/bite"
        get_bite = get(api)
        get_json = get_bite.json()
        get_gif_url = get_json["url"]
        await message.reply_video(get_gif_url)
    except:
        pass

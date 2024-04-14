from requests import get
from pyrogram import filters
from pyrogram.types import Message
from DAXXMUSIC import app

@app.on_message(filters.command("hug"))
async def es_url(_, message):
    try:
        api = "https://api.waifu.pics/sfw/hug"
        get_hug = get(api)
        get_json = get_hug.json()
        get_gif_url = get_json["url"]
        await message.reply_video(get_gif_url)
    except:
        pass

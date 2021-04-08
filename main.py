
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import serve
ostrich = Client("theostrich",
             bot_token="1758679986:AAGNhFP4hDTXibaLCxi3erYpDEo5fI3Z7mo",
             api_id=2137624,
             api_hash="fe9829e648f0e535da81aaad34b7e8e0")

@ostrich.on_message(filters.private & (filters.document | filters.video))
async def cc(client,message):
  msg = await client.send_message(chat_id=message.chat.id, text="Downloading your file yo my server...")
  download_loc = await client.download_media(
        message)
  await msg.edit_text(download_loc)

serve.keep_alive()
ostrich.run()


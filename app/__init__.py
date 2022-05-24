import os
import logging
from dotenv import load_dotenv
from telethon import TelegramClient


load_dotenv()
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
# print(api_id, api_hash, bot_token)


class Bot(TelegramClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.me = None


bot = Bot('bot', api_id, api_hash)
bot.parse_mode = 'HTML'
logging.basicConfig(level=logging.INFO)


import app.handlers


async def start():
    await bot.connect()
    bot.me = await bot.sign_in(bot_token=bot_token)
    await bot.run_until_disconnected()


def run():
    bot.loop.run_until_complete(start())

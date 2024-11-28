from aiogram import Dispatcher, types, Bot 
from aiogram.filters import CommandStart
from aiogram.types import Message

async def user_info(message: Message, bot: Bot):
    user = await bot.get_chat(message.from_user.id)
    
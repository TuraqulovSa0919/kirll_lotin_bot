import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import API_TOKEN
from my_database import insert_user
from transliterate import to_cyrillic, to_latin
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    user = await bot.get_chat(message.from_user.id)
    full_namei = message.from_user.full_name
    username = message.from_user.username if message.from_user.username else 'None'
    bio = user.bio if user.bio else 'bio Mavjud emas!!!'
    user_ID = message.from_user.id
    try:
        insert_user(full_namei, username, bio, user_ID)
        text_about = 'Matn kiriting: '
        await message.answer(text_about)
    except Exception as e:
        await message.answer(f"Xatolik yuz berdi: {e}")


@dp.message()
async def echo(message: types.Message):
    text = message.text
    if text.isascii():
        change = to_cyrillic(text)
    else:
        change = to_latin(text)
    await message.answer(change)


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
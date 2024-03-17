from aiogram import types
from bot import router
from aiogram.filters import CommandStart

class StartCommandHandler:
    @router.message(CommandStart())
    async def start(message: types.Message):
        await message.reply("Привет Бро я МАРС")
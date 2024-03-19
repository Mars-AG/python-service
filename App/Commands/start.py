from aiogram import types, Router
from aiogram.filters import CommandStart, Command
from App.PIL.PILService import PILService
from Database.db import Database
from Database.Handlers.DatabaseHandlers import DatabaseHandlers
from aiogram.types import FSInputFile
import os

startRouter = Router()
db = Database()
RESOURCE_PATH = "./App/Commands/Resources/"

class StartCommandHandler:
    def registration(user_id):
        DatabaseHandlers.registration(user_id)

    def generation_photo(user_id, username):
        user = DatabaseHandlers.user(user_id)

        fonts = [
            {'font': f'{RESOURCE_PATH}BarlowRegular.ttf', 'size': 48},
            {'font': f'{RESOURCE_PATH}BarlowMedium.ttf', 'size': 36} 
        ]

        bg_image = f"{RESOURCE_PATH}card_bg.png"
        PILService.get_photo(user[0][2], username, fonts, bg_image)

    @staticmethod
    @startRouter.message(CommandStart())
    async def start(message: types.Message):
        user_id = message.from_user.id

        StartCommandHandler.registration(user_id)
        StartCommandHandler.generation_photo(user_id, message.chat.username)

        photo = FSInputFile("temp_image.png")
        caption = f"Приветствую {message.chat.first_name}! Твой профиль 👆"
        await message.answer_photo(photo=photo, caption=caption)

        os.remove("temp_image.png")

from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from Database.db import Database

startRouter = Router()
db = Database()

class StartCommandHandler:
    @staticmethod
    @startRouter.message(Command("hello"))
    async def start(message: types.Message):
        await message.reply(f"Приветвую, {message.chat.username}!")

    @staticmethod
    def get_yes_no_kb() -> ReplyKeyboardMarkup:
        kb = ReplyKeyboardBuilder()
        kb.button(text="Да")
        kb.button(text="Нет")
        kb.adjust(2)
        return kb.as_markup(resize_keyboard=True)

    @staticmethod
    @startRouter.message(CommandStart())
    async def start(message: types.Message):

        try:
            sql_query = "INSERT INTO users (user_id, user_level) VALUES (%s, %s)"
            data_to_insert = [
                (message.from_user.id, 0),
            ]
            db.execute_query(sql_query, data_to_insert)
            db.close_connection()
            await message.reply('Успешная Регистрация')
        except:
            await message.reply('Регистрация не прошла')

        await message.answer(
            "Вы довольны нашей работой?",
            reply_markup=StartCommandHandler.get_yes_no_kb()
        )

    @staticmethod
    @startRouter.message(F.text.lower() == "да")
    async def answer_yes(message: types.Message):
        await message.answer(
            "Это здорово!",
            reply_markup=ReplyKeyboardRemove()
        )

    @staticmethod
    @startRouter.message(F.text.lower() == "нет")
    async def answer_no(message: types.Message):
        await message.answer(
            "Иди нахуй, мудак!",
            reply_markup=ReplyKeyboardRemove()
        )
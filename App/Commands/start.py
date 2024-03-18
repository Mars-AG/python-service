from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from Database.db import Database

startRouter = Router()
db = Database()

class StartCommandHandler:
    @startRouter.message(Command("hello"))
    async def start(message: types.Message):
        await message.reply(f"Приветвую, {message.chat.username}!")

    def get_yes_no_kb() -> ReplyKeyboardMarkup:
        kb = ReplyKeyboardBuilder()
        kb.button(text="Да")
        kb.button(text="Нет")
        kb.adjust(2)
        return kb.as_markup(resize_keyboard=True)

    @startRouter.message(CommandStart())
    async def start(self):

        try:
            sql_query = "INSERT INTO users (user_id, user_level) VALUES (%s, %s)"
            data_to_insert = [
                (123456, 0),
            ]
            db.execute_query(sql_query, data_to_insert)
            db.close_connection()
        except:
            print('Регистрация не прошла')

    @startRouter.message(F.text.lower() == "да")
    async def answer_yes(message: types.Message):
        await message.answer(
            "Это здорово!",
            reply_markup=ReplyKeyboardRemove()
        )

    @startRouter.message(F.text.lower() == "нет")
    async def answer_no(message: types.Message):
        await message.answer(
            "Иди нахуй, мудак!",
            reply_markup=ReplyKeyboardRemove()
        )
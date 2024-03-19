from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from Database.db import Database
from Database.Handlers.DatabaseHandlers import DatabaseHandlers

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
        DatabaseHandlers.registration(message.from_user.id)
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
            "Жаль... :(",
            reply_markup=ReplyKeyboardRemove()
        )
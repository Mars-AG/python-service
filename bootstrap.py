import logging
import sys
from aiogram import Dispatcher
from App.Bots.Mars.bot import BotMars, router
from App.Commands.start import startRouter
from Config.EnvService import Env
from aiohttp import web

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    bot = BotMars(Env.get("BOT_TOKEN"), Dispatcher(), web.Application())
    bot.commands(router, startRouter)
    bot.boot()
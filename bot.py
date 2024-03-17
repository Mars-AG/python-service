import logging
import sys
from typing import List
from aiohttp import web
from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from Config.EnvService import Env
from Config.ServerService import Server

router = Router()

class BotMars(Bot):
    WEBHOOK_PATH = Server.createWebhookPATH(Env.get("BOT_TOKEN"))
    APP = app = web.Application()

    def __init__(self, token, dp):
        self.TOKEN = token
        self.DP = dp
        self.BASEBOT =  Bot(
                            self.TOKEN, 
                            parse_mode=ParseMode.HTML, 
                            session=Server.getServerSession()
                        )

    async def on_startup(self):
        await self.BASEBOT.set_webhook(
            url=f"{Server.getWebhookURL()}{self.WEBHOOK_PATH}",
            drop_pending_updates=True
        )
        webhook_requests_handler = SimpleRequestHandler(dispatcher=self.DP, bot=self.BASEBOT,)
        webhook_requests_handler.register(self.APP, path=self.WEBHOOK_PATH)

    def webhook_handler(self):
        setup_application(self.APP, self.DP, bot=self.BASEBOT)
        web.run_app(self.APP, host=Server.getServerHost(), port=int(Server.getServerPort()))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    dp = Dispatcher()
    dp.include_router(router)
    bot = BotMars(Env.get("BOT_TOKEN"), dp)
    dp.startup.register(bot.on_startup)
    bot.webhook_handler()

    from App.start import start
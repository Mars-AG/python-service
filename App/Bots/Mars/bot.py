from aiogram import Bot, Router
from aiogram.enums import ParseMode
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from Config.ConnectService import ConnectService
from aiohttp import web

router = Router()

class BotMars(Bot):
    def __init__(self, token, dp, app):
        self.TOKEN = token
        self.DP = dp
        self.APP = app
        self.BASEBOT =  Bot(
                            self.TOKEN, 
                            parse_mode=ParseMode.HTML, 
                            session=ConnectService.getSession()
                        )
        
    def commands(self, *routes: Router):
        self.DP.include_routers(*routes)

    async def webhook_handler(self):
        await self.BASEBOT.set_webhook(
            url=f"{ConnectService.getWebhookURL()}{ConnectService.getWebhookPATH(self.TOKEN)}",
            drop_pending_updates=True
        )
        webhook_requests_handler = SimpleRequestHandler(dispatcher=self.DP, bot=self.BASEBOT)
        webhook_requests_handler.register(self.APP, path=ConnectService.getWebhookPATH(self.TOKEN))

    def boot(self):
        self.DP.startup.register(self.webhook_handler)

        setup_application(self.APP, self.DP, bot=self.BASEBOT)
        web.run_app(
            self.APP, 
            host=ConnectService.getHost(), 
            port=int(ConnectService.getPort())
        )
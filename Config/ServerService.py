from Config.EnvService import Env
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer

class Server:
    @staticmethod
    def getWebhookURL():
        return Env.get("BASE_WEBHOOK_URL")
    
    @staticmethod
    def getServerHost():
        return Env.get("WEB_SERVER_HOST")
    
    @staticmethod
    def getServerPort():
        return Env.get("WEB_SERVER_PORT")
    
    @staticmethod
    def getServerSession():
        return AiohttpSession(
            api=TelegramAPIServer.from_base(Env.get("API"))
        )
    
    @staticmethod
    def createWebhookPATH(token):
        return f"/{token}/webhook"
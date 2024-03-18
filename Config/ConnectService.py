from Config.EnvService import Env
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer

class ConnectService:
    @staticmethod
    def getWebhookURL():
        return Env.get("APP_URL")
    
    @staticmethod
    def getHost():
        return Env.get("WEB_SERVER_HOST")
    
    @staticmethod
    def getPort():
        return Env.get("WEB_SERVER_PORT")
    
    @staticmethod
    def getSession():
        return AiohttpSession(
            api=TelegramAPIServer.from_base(Env.get("TELEGRAM_SERVER"))
        )
    
    @staticmethod
    def getWebhookPATH(token):
        return f"/{token}/webhook"
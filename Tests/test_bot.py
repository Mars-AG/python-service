from unittest.mock import AsyncMock
import pytest
from bot import MyBot
from dotenv import load_dotenv
import os
load_dotenv()

@pytest.fixture
def bot():
    return MyBot(os.getenv("BOT_TOKEN"))

@pytest.mark.asyncio
async def test_start_handler(bot):
    message = AsyncMock()
    await bot.start(message) 
    message.reply.assert_called_with("Привет Бро я МАРС")
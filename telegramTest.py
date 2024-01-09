import telegram
import asyncio

bot = telegram.Bot(token="")
chat_id = ""

asyncio.run(bot.sendMessage(chat_id=chat_id, text="파이썬 텔레그램 테스트!!"))

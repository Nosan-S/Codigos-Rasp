from aiogram import Bot
import asyncio

API_TOKEN = "7470994115:AAHKCknsAbixK6RqIXpNucZOoZh6ca_ZPNg"
CHAT_ID = "1324582704"

async def send_message():
    bot = Bot(token=API_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="Hello, this is a test message!")
    await bot.session.close()
    print("Message sent successfully!")

if __name__ == "__main__":
    asyncio.run(send_message())
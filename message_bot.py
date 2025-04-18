import asyncio
import sqlite3
from datetime import datetime
from aiogram import Bot

def run_message():
	
	API_TOKEN = '7470994115:AAHKCknsAbixK6RqIXpNucZOoZh6ca_ZPNg'
	CHAT_ID = '1324582704t'
	bot = Bot(token=API_TOKEN)

	conn = sqlite3.connect("sensor_info.db")
	cursor = conn.cursor()

	now = datetime.now()

	day = now.strftime("%A %d %B %Y")
	time = now.strftime("%H:%M:%S")

	cursor.execute("SELECT valor FROM sensors WHERE sensor = ?", ("hume1",))
	Shume1 = cursor.fetchone()[0]
	print(Shume1)
	cursor.execute("SELECT valor FROM sensors WHERE sensor = ?", ("hume2",))
	Shume2 = cursor.fetchone()[0]
	cursor.execute("SELECT valor FROM sensors WHERE sensor = ?", ("hume3",))
	Shume3 = cursor.fetchone()[0]
	cursor.execute("SELECT valor FROM sensors WHERE sensor = ?", ("humA",))
	ShumeA = cursor.fetchone()[0]	
	cursor.execute("SELECT valor FROM sensors WHERE sensor = ?", ("luzA",))
	SluzA = cursor.fetchone()[0]
	cursor.execute("SELECT valor FROM sensors WHERE sensor = ?", ("tempA",))
	StempA = cursor.fetchone()[0]


	async def send_message():
		async with Bot(token=API_TOKEN) as bot:
			await bot.send_message(CHAT_ID, f"{day}\t{time}")
			await bot.send_message(CHAT_ID, f"Humedad Cultivo 1: {Shume1} \nHumedad Cultivo 2: {Shume2} \nHumedad Cultivo 3: {Shume3}")
			await bot.send_message(CHAT_ID, f"Temperatura: {StempA} \n Humedad ambiental: {ShumeA} \n Luz ambiental: {SluzA}")


	if __name__ == '__main__':

		asyncio.run(send_message())
run()
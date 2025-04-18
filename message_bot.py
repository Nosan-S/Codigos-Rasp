from aiogram import Bot
from datetime import datetime
from analog_sensor import read_hume, read_luz
from digital_sensor import read_digital
import asyncio

API_TOKEN = "7470994115:AAHKCknsAbixK6RqIXpNucZOoZh6ca_ZPNg"
CHAT_ID = "1324582704"

async def send_message(chat_id, message):
    bot = Bot(token=API_TOKEN)
    await bot.send_message(chat_id, message)
    await bot.session.close()  # Close the session after sending the message
    print("[-] Message sent")

def get_sensor_values():
    shume1, shume2, shume3 = read_hume()
    sluzA = read_luz()
    stempA, shumeA = read_digital()
    return shume1, shume2, shume3, sluzA, stempA, shumeA

async def run_message():
    now = datetime.now()
    day = now.strftime("%A %d %B %Y")
    time = now.strftime("%H:%M:%S")
    var1, var2, var3, var4, var5, var6 = get_sensor_values()
    mensaje = f"{day}\t{time}\nHumedad Cultivo 1: {var1} \nHumedad Cultivo 2: {var2} \nHumedad Cultivo 3: {var3}\nLuz Ambiental: {var4} \nTemperatura ambiental: {var5} \nHumedad ambiental: {var6}"
    await(send_message(CHAT_ID, mensaje))
    print("[-] Done")

if __name__ == '__main__':
    asyncio.run(run_message())
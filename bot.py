#SUNRISES24BOTS
#TG:@SUNRISES_24
from pyrogram import Client
from config import *
import os

class Bot(Client):
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)

    def __init__(self):
        super().__init__(
            name="MMWREN",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=100,
            plugins={"root": "main"},
            sleep_threshold=10,
        )
    async def start(self):
        await super().start()
        me = await self.get_me()      
        await self.send_message(chat_id=int(ADMIN), text="Re𝚂𝚃𝙰𝚁𝚃𝙴𝙳.. ❤️‍🩹")
        print(f"{me.first_name} | @{me.username} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳...⚡️")
        
    async def stop(self, *args):
       await self.send_message(chat_id=int(ADMIN), text="Stopped Please Restart Me...!!!")
       await super().stop()      
       print("Bot Restarting........")


bot = Bot()
bot.run()

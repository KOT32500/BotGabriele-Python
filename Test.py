import discord
import BazaDate
import time
import random
import asyncio
import aiohttp
from botFunctions import *

class Error():
    pass

def is_internet():
    """
    Query internet using python
    :return:
    """
    
    try:
        urlopen('https://www.google.com', timeout=1)
        
        return True
    except urllib.error.URLError:
        return False
def InternetActive():
    client = MyClient()
    try:
        client.run(BazaDate.token)
    except: 
        print("Нет подключения к интернету")
class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Loggined")
        Guild = await self.fetch_guild(419879599363850251)
        Talant_ = Talant("KOT32500")
        Talant_.PickTalant("Героический уровень")
        Task1 = asyncio.create_task(Talant_._Update())
        asyncio.gather(Task1)







InternetActive()

while True:
    time.sleep(1)
    if is_internet():
        if(internetWasOff == True):
            print("Internet is active")
            InternetActive()
            internetWasOff = False
    else:
        internetWasOff = True
from random import random
import aiohttp
import random

class Comic():

    def __init__(self):
        randomNumber = random.randint(1,2491)
        self.base_url = "https://xkcd.com/"+str(randomNumber)+"/info.0.json"
    
    async def get_comic_url(self):
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url
            async with session.get(base_url) as repo:
                comicJson = await repo.json()
                return comicJson["img"]
    
    async def get_comic_title(self):
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url
            async with session.get(base_url) as repo:
                comicJson = await repo.json()
                return comicJson["safe_title"]

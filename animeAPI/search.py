import aiohttp

class AnimeSearch():

    def __init__(self,what:str):
        self.base_url = "https://api.jikan.moe/v3/search/" + what +  "?q="
    
    async def searchAnime(self,anime_name = None):
        if anime_name == None:
            return 0
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url + anime_name
            async with session.get(base_url) as repo:
                resultJson = await repo.json()
                return resultJson["results"]
    
    async def searchAnime1(self,anime_name = None):
        if anime_name == None:
            return 0
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url + anime_name
            async with session.get(base_url) as repo:
                resultJson = await repo.json()
                first_search = resultJson["results"]
                return first_search[0]
    
    async def searchManga(self,anime_name = None):
        if anime_name == None:
            return 0
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url + anime_name
            async with session.get(base_url) as repo:
                resultJson = await repo.json()
                return resultJson["results"]
    
    async def searchManga1(self,anime_name = None):
        if anime_name == None:
            return 0
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url + anime_name
            async with session.get(base_url) as repo:
                resultJson = await repo.json()
                first_search = resultJson["results"]
                return first_search[0]
import aiohttp

class GetGif():

    def __init__(self):
        self.base_url = "https://g.tenor.com/v1/search?q=among%20us&key=Y90QF5A0KU8E&limit=51"
    
    async def amongusGIF(self):
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url
            async with session.get(base_url) as repo:
                comicJson = await repo.json()
                return comicJson["results"]
    
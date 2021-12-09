import aiohttp

class Quotes():

    def __init__(self):
        self.base_url = "https://animechan.vercel.app/api/random"
    
    async def random_quotes(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url) as repo:
                resultJson = await repo.json()
                return resultJson
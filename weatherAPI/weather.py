import aiohttp

class checker():

    def __init__(self):
        self.base_url = "http://api.weatherapi.com/v1/current.json?key=a13a1efd11c346a6bfa80929211508&q="
    
    async def get_weather(self,search_what):
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url + search_what
            async with session.get(base_url) as repo:
                resultJson = await repo.json()
                return resultJson

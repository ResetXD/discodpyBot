import aiohttp

class chatbot():

    def __init__(self):
        self.base_url = "https://api.popcatdev.repl.co/chatbot?msg="
    
    async def get_response(self,message):
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url + message + "&owner=reset&botname=resetBot"
            async with session.get(base_url) as repo:
                comicJson = await repo.json()
                return comicJson["response"]
    
    async def get_meme(self):
        async with aiohttp.ClientSession() as session:
            base_url = "https://api.popcatdev.repl.co/meme"
            async with session.get(base_url) as repo:
                comicJson = await repo.json()
                return comicJson["image"]
    
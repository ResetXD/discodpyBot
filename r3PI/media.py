import aiohttp

class GetGif():

    def __init__(self):
        self.base_url = "https://rule34.xxx/index.php?page=dapi&s=post&q=index&topic=dapi&json=1&tags="
    
    async def get_(self,tag):
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url + tag + "*"
            async with session.get(base_url) as repo:
                comicJson = await repo.json()
                return comicJson
    
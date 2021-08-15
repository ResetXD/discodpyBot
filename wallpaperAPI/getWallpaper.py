import aiohttp

class getWallpaper():

    def __init__(self):
        self.base_url = "https://wallhaven.cc/api/v1/search?q="
    
    async def get_wallpaper_by_tag(self,tag):
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url + str(tag)
            async with session.get(base_url) as repo:
                comicJson = await repo.json()
                return comicJson["data"]
    
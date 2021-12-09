import aiohttp

class getIMAGE():

    def __init__(self):
        self.base_url = "https://danbooru.donmai.us/posts.json?tags="
    
    async def get_random(self):
        async with aiohttp.ClientSession() as session:
            base_url = "https://danbooru.donmai.us/posts/random.json"
            async with session.get(base_url) as repo:
                rawJSON = await repo.json()
                return rawJSON["file_url"]
    
    async def get_by_tag(self,tag):
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url + str(tag)
            async with session.get(base_url) as repo:
                rawJSON = await repo.json()
                return rawJSON
    
    async def search_tag(self,search):
        async with aiohttp.ClientSession() as session:
            base_url = "https://danbooru.donmai.us/tags.json?search[name_matches]=" + str(search) + "*"
            async with session.get(base_url) as repo:
                rawJSON = await repo.json()
                return rawJSON

    
    
    
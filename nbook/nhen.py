import aiohttp

class NHEN_json():

    def __init__(self):
        self.base_url = "https://nhentai.net/"
    
    async def get_rawJSON(self,id):
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url + "/api/gallery/" + str(id)
            async with session.get(base_url) as repo:
                rawJSON = await repo.json()
                return rawJSON
    
    
    
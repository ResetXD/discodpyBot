import aiohttp

class NHEN_IMG():

    def __init__(self):
        self.base_url = "https://i.nhentai.net/galleries/"
    
    async def get_page(self,id,page):
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url + str(id) +"/"+ str(page) + ".jpg"
            async with session.get(base_url) as repo:
                if repo.status == 200:
                    return base_url
                else:
                    return self.base_url + str(id) +"/"+ str(page) + ".png"
    
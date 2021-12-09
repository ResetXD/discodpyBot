import aiohttp

class MANGA_IMG():

    def __init__(self):
        self.base_url = "https://img.mghubcdn.com/file/imghub/"
    
    async def get_page(self,manga_name,chapter,page):
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url + str(manga_name) +"/"+str(chapter)+"/"+str(page) + ".jpg"
            async with session.get(base_url) as repo:
                if repo.status == 200:
                    return base_url
                else:
                    base_url = self.base_url + str(manga_name) +"/"+str(chapter)+"/"+str(page) + ".png"
                    async with session.get(base_url) as repo:
                        if repo.status == 200:
                            return base_url
                        else:
                            return "https://media.discordapp.net/attachments/862233532716941315/862264610610348043/3759075.jpg?width=725&height=663"
    
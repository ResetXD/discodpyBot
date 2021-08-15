import aiohttp

class imageGrabber():

    def __init__(self):
        self.base_url = "https://nekobot.xyz/api/"
    
    async def get_image(self,imgType=None):
        if imgType == None:
            return 0
        else:
            async with aiohttp.ClientSession() as session:
                base_url = self.base_url +"image?type="+ str(imgType)
                try:
                    async with session.get(base_url) as repo:
                        comicJson = await repo.json()
                        return comicJson["message"]
                except:
                    async with session.get(base_url) as repo:
                        comicJson = await repo.json(content_type='text/html')
                        return comicJson["message"]

    
    async def get_imagegen(self,imgType=None,image=None):
        if imgType == None or image == None:
            return 0
        else:
            async with aiohttp.ClientSession() as session:
                base_url = self.base_url +"imagegen?type="+ str(imgType)+"&image="+str(image)
                try:
                    async with session.get(base_url) as repo:
                        comicJson = await repo.json()
                        return comicJson["message"]
                except:
                    async with session.get(base_url) as repo:
                        comicJson = await repo.json(content_type='text/html')
                        return comicJson["message"]
    
    async def get_imagegenURL(self,imgType=None,image=None):
        if imgType == None or image == None:
            return 0
        else:
            async with aiohttp.ClientSession() as session:
                base_url = self.base_url +"imagegen?type="+ str(imgType)+"&url="+str(image)
                try:
                    async with session.get(base_url) as repo:
                        comicJson = await repo.json()
                        return comicJson["message"]
                except:
                    async with session.get(base_url) as repo:
                        comicJson = await repo.json(content_type='text/html')
                        return comicJson["message"]
    
    async def get_imagegen_phcomment(self,imgType=None,image=None,text=None,username=None):
        if imgType == None or image == None or text == None or username == None:
            return 0
        else:
            async with aiohttp.ClientSession() as session:
                base_url = self.base_url +"imagegen?type="+ str(imgType)+"&image="+str(image)+"&text="+str(text)+"&username="+str(username)
                try:
                    async with session.get(base_url) as repo:
                        comicJson = await repo.json()
                        return comicJson["message"]
                except:
                    async with session.get(base_url) as repo:
                        comicJson = await repo.json(content_type='text/html')
                        return comicJson["message"]
    
    async def get_imagegen_tweet(self,imgType=None,text=None,username=None):
        if imgType == None or text == None or username == None:
            return 0
        else:
            async with aiohttp.ClientSession() as session:
                base_url = self.base_url +"imagegen?type="+ str(imgType)+"&text="+str(text)+"&username="+str(username)
                try:
                    async with session.get(base_url) as repo:
                        comicJson = await repo.json()
                        return comicJson["message"]
                except:
                    async with session.get(base_url) as repo:
                        comicJson = await repo.json(content_type='text/html')
                        return comicJson["message"]
    
    async def get_imagegen_kanna(self,imgType=None,text=None):
        if imgType == None or text == None:
            return 0
        else:
            async with aiohttp.ClientSession() as session:
                base_url = self.base_url +"imagegen?type="+ str(imgType)+"&text="+str(text)
                try:
                    async with session.get(base_url) as repo:
                        comicJson = await repo.json()
                        return comicJson["message"]
                except:
                    async with session.get(base_url) as repo:
                        comicJson = await repo.json(content_type='text/html')
                        return comicJson["message"]
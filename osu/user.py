import aiohttp

class User():

    def __init__(self,token):
        self.key = token.key
        self.base_url = "https://osu.ppy.sh/api/"
    
    async def get_user(self,username="peppy",mode = 0):
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url+"get_user?k="+str(self.key)+"&u="+str(username)+"&m="+str(mode)
            async with session.get(base_url) as repo:
                userJson = await repo.json()
                return userJson[0]
    
    def get_user_pfp_url(self,user_id = None):
        if user_id == None:
            return 0
        else:
            return f"http://s.ppy.sh/a/{str(user_id)}"

    async def get_user_recent(self,username="peppy",mode = 0):
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url+"get_user_recent?k="+str(self.key)+"&u="+str(username)+"&m="+str(mode)
            async with session.get(base_url) as repo:
                recentJson = await repo.json()
                if len(recentJson) == 0:#tells if no best map played
                    return 0
                return recentJson[0]

    async def get_user_best_one(self,username="peppy",mode = 0):
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url+"get_user_best?k="+str(self.key)+"&u="+str(username)+"&m="+str(mode)
            async with session.get(base_url) as repo:
                bestJson = await repo.json()
                return bestJson[0]
    
    async def get_user_best_ten(self,username="peppy",mode = 0):
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url+"get_user_best?k="+str(self.key)+"&u="+str(username)+"&m="+str(mode)
            async with session.get(base_url) as repo:
                bestJson = await repo.json()
                return bestJson
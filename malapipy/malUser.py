import aiohttp
from malapipy import mal_client


class user():
    def __init__(self,client:mal_client.Client) -> None:
        self.header = client.header
        
    async def userInfo(self,user_id="1627723200"):
        """
        more like search results with parameters query as string,offset(no one cares),limit of how much to retrive
        returns a dictionary inside a list with dictionary having first key as "node" which have a dictionary inside it
        which have keys such as "id","title","main_picture"->"medium","large"
        example of getting the first title as "data[0]["node"]["title"]" with data being the returned data
        """
        async with aiohttp.ClientSession(headers=self.header) as session:
            url = f"https://api.myanimelist.net/v2/users/{user_id}?fields=anime_statistics"
            async with session.get(url) as repo:
                a = await repo.json()
                return a
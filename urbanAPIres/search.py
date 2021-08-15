import aiohttp

class Search():

    def __init__(self):
        self.base_url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
        self.headers = {
                        'x-rapidapi-key': "no",
                        'x-rapidapi-host': "no"
                       }
    
    async def get_search(self,search_what):
        params = {"term":str(search_what)}
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(self.base_url,params=params) as repo:
                resultJson = await repo.json()
                return resultJson

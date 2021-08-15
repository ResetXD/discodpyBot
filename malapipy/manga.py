import aiohttp
from malapipy import mal_client
class manga():
    def __init__(self,client:mal_client.Client) -> None:
        self.header = client.header
        
    async def manga_list(self,query,offset=0,limit=5):
        """
        more like search results with parameters query as string,offset(no one cares),limit of how much to retrive
        returns a dictionary inside a list with dictionary having first key as "node" which have a dictionary inside it
        which have keys such as "id","title","main_picture"->"medium","large"
        example of getting the first title as "data[0]["node"]["title"]" with data being the returned data
        """
        async with aiohttp.ClientSession(headers=self.header) as session:
            url = f"https://api.myanimelist.net/v2/manga?q={query}&limit={limit}&offset={offset}"
            async with session.get(url) as repo:
                a = await repo.json()
                return a["data"]
    


    async def mangaDetail_ID(self,query):
        """
        give id get details EZ
        return a dict to know its keys/(structure of the dict) go here ->
        """
        async with aiohttp.ClientSession(headers=self.header) as session:
            url = f"https://api.myanimelist.net/v2/manga/{query}?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_volumes,num_chapters,authors,pictures,background,related_anime,related_manga,recommendations,serialization"
            async with session.get(url) as repo:
                a = await repo.json()
                return a
    
    async def mangaDetail_name(self,query,offset=0):
        """
        takes the "name" gives that to method anime_list gets the first result gets that id and then gives that to get_animeDetail_with_ID
        returns a dict with the same structure as of get_animeDetail_With_ID
        """
        a = await self.manga_list(query,offset,1)
        id = a[0]["node"]["id"]
        b = await self.mangaDetail_ID(str(id))
        return b

    async def anime_ranking(self,ranking_type="all",limit=10,offset=0):
        """
        parameter "ranking_type" can only be all,manga,oneshots,doujin,lightnovels,novels,manhwa,manhua,bypopularity,favorite
        returns a dictionary(s) inside a list with dictionary having first key as "node" which have a dictionary inside it
        which have keys such as "id","title","main_picture"->"medium","large"
        example of getting the first title as "data[0]["node"]["title"]" with data being the returned data
        """
        async with aiohttp.ClientSession(headers=self.header) as session:
            url = f"https://api.myanimelist.net/v2/manga/ranking?ranking_type={ranking_type}&limit={limit}&offset={offset}"
            async with session.get(url) as repo:
                a = await repo.json()
                return a["data"]
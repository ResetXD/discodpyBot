import aiohttp
from malapipy import mal_client


class anime():
    def __init__(self,client:mal_client.Client) -> None:
        self.header = client.header
        
    async def anime_list(self,query,offset=0,limit=5):
        """
        more like search results with parameters query as string,offset(no one cares),limit of how much to retrive
        returns a dictionary inside a list with dictionary having first key as "node" which have a dictionary inside it
        which have keys such as "id","title","main_picture"->"medium","large"
        example of getting the first title as "data[0]["node"]["title"]" with data being the returned data
        """
        async with aiohttp.ClientSession(headers=self.header) as session:
            url = f"https://api.myanimelist.net/v2/anime?q={query}&limit={limit}&offset={offset}"
            async with session.get(url) as repo:
                a = await repo.json()
                return a["data"]
    


    async def animeDetail_ID(self,query):
        """
        give id get details EZ
        return a dict to know its keys/(structure of the dict) go here ->
        """
        async with aiohttp.ClientSession(headers=self.header) as session:
            url = f"https://api.myanimelist.net/v2/anime/{query}?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,recommendations,studios,statistics"
            async with session.get(url) as repo:
                a = await repo.json()
                return a
    
    async def animeDetail_name(self,query,offset=0):
        """
        takes the "name" gives that to method anime_list gets the first result gets that id and then gives that to get_animeDetail_with_ID
        returns a dict with the same structure as of get_animeDetail_With_ID
        """
        a = await self.anime_list(query,offset,1)
        id = a[0]["node"]["id"]
        b = await self.animeDetail_ID(str(id))
        return b

    async def anime_ranking(self,ranking_type="all",limit=10,offset=0):
        """
        parameter "ranking_type" can only be all,airing,upcoming,tv,ova,movie,special,bypopularity,favorite
        returns a dictionary(s) inside a list with dictionary having first key as "node" which have a dictionary inside it
        which have keys such as "id","title","main_picture"->"medium","large"
        example of getting the first title as "data[0]["node"]["title"]" with data being the returned data
        """
        async with aiohttp.ClientSession(headers=self.header) as session:
            url = f"https://api.myanimelist.net/v2/anime/ranking?ranking_type={ranking_type}&limit={limit}&offset={offset}"
            async with session.get(url) as repo:
                a = await repo.json()
                return a["data"]
    
    async def anime_seasonal(self,year=2020,season="summer",sort="anime_score",limit=5,offset=0):
        """
        parameter "sort" can only be anime_score OR anime_num_list_users
        season can only be  winter,spring,summer,fall
        returns a dictionary(s) inside a list with dictionary having first key as "node" which have a dictionary inside it
        which have keys such as "id","title","main_picture"->"medium","large"
        example of getting the first title as "data[0]["node"]["title"]" with data being the returned data
        """
        async with aiohttp.ClientSession(headers=self.header) as session:
            url = f"https://api.myanimelist.net/v2/anime/season/{year}/{season}?limit={limit}&sort={sort}&offset={offset}"
            async with session.get(url) as repo:
                a = await repo.json()
                return a["data"]
    

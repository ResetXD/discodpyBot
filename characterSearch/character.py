import aiohttp

class char():
    
    async def by_char_name(self,name):
        head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"}
        async with aiohttp.ClientSession(headers=head) as session:
            base_url = f"https://www.animecharactersdatabase.com/api_series_characters.php?character_q={str(name)}"
            async with session.get(base_url) as repo:
                rawJSON = await repo.json()
                return rawJSON["search_results"]
    
    async def by_char_id(self,name):
        head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"}
        async with aiohttp.ClientSession(headers=head) as session:
            base_url = "https://www.animecharactersdatabase.com/api_series_characters.php?character_id=" + str(name)
            async with session.get(base_url) as repo:
                rawJSON = await repo.json()
                return rawJSON
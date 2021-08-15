import aiohttp


class Beatmap():
    def __init__(self,token):
        self.key = token.key
        self.base_url = "https://osu.ppy.sh/api/"

    async def get_beatmap(self,beatmapID=None):
        if beatmapID == None:#to check if a id is passed
            return 0
        async with aiohttp.ClientSession() as session:
            base_url = self.base_url+"get_beatmaps?k="+str(self.key)+"&b="+str(beatmapID)
            async with session.get(base_url) as repo:
                beatmapJson = await repo.json()
                return beatmapJson[0]
    
    def get_beatmap_thumbnail_url(self,beatmapset_id=None):
        if beatmapset_id == None:
            return 0
        else:
            return f"https://b.ppy.sh/thumb/{beatmapset_id}l.jpg"
    
    def get_beatmap_cover_url(self,beatmapset_id=None):
        if beatmapset_id == None:
            return 0
        else:
            return f"https://assets.ppy.sh/beatmaps/{beatmapset_id}/covers/cover.jpg"

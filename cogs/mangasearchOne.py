import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from animeAPI import search

class searchAni(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def manga(self, ctx:Context,*,anime_name = None):
        if anime_name == None:
            await ctx.channel.send("what do i even search")
            return
        a = search.AnimeSearch("manga")
        c = await a.searchManga(anime_name)
        c = c[0]
        animeTitle = c["title"]
        animeURL = c["url"]
        animeScore = c["score"]
        animeType = c["type"]
        animeStart = c["start_date"]
        animeEnd = c["end_date"]
        if animeStart == None:
            animeStart = "idk"
        if animeEnd == None:
            animeEnd = "idk"
        animeEpisode = c["chapters"]
        animeVolumes = c["volumes"]
        animeSynopsis = c["synopsis"]
        animeImage = c["image_url"]
        embedVar = discord.Embed(color = discord.Colour.dark_theme())
        embedVar.add_field(name = "title" , value = f"[{animeTitle}]({animeURL})")
        embedVar.add_field(name = "MAL score" , value = animeScore)
        embedVar.add_field(name = "type" , value = animeType)
        embedVar.add_field(name = "started" , value = animeStart[0:10])
        embedVar.add_field(name = "ended" , value = animeEnd[0:10])
        embedVar.add_field(name = "chapters" , value = animeEpisode)
        embedVar.add_field(name = "volume" , value = animeVolumes)
        embedVar.add_field(name = "synopsis" , value = animeSynopsis)
        embedVar.set_thumbnail(url = animeImage)
        await ctx.channel.send(embed = embedVar)
    
    @manga.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(searchAni(client))
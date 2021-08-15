import discord
from animeAPI import search
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.ext.commands.cooldowns import BucketType


class searchAni(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['anime'])
    async def ani(self, ctx:Context,*,anime_name = None):
        if anime_name == None:
            await ctx.channel.send("what do i even search")
            return
        a = search.AnimeSearch("anime")
        c = await a.searchAnime1(anime_name)
        animeTitle = c["title"]
        animix = animeTitle.replace(" ","-")
        animix = animix.lower()
        animixplay = "https://animixplay.to/v1/"+animix
        anime9 = "https://4anime.to/anime/" + animix
        hanime = "https://hanime.tv/videos/hentai/" + animix + "-1"
        animeURL = c["url"]
        animeScore = c["score"]
        animeType = c["type"]
        animeStart = c["start_date"]
        animeEnd = c["end_date"]
        if animeStart == None:
            animeStart = "idk"
        if animeEnd == None:
            animeEnd = "idk"
        animeEpisode = c["episodes"]
        animeSynopsis = c["synopsis"]
        animeImage = c["image_url"]
        animeRated = c["rated"]
        if animeRated == "Rx":
            embedVar = discord.Embed(color = discord.Colour.dark_theme())
            embedVar.add_field(name = "title" , value = f"[{animeTitle}]({animeURL})")
            embedVar.add_field(name = "MAL score" , value = animeScore)
            embedVar.add_field(name = "type" , value = animeType)
            embedVar.add_field(name = "started" , value = animeStart[0:10])
            embedVar.add_field(name = "ended" , value = animeEnd[0:10])
            embedVar.add_field(name = "no of episodes" , value = animeEpisode)
            embedVar.add_field(name = "synopsis" , value = animeSynopsis)
            embedVar.add_field(name = "rated" , value = animeRated)
            embedVar.add_field(name = "possible hentai link" , value = f"[hanime]({hanime})")
            embedVar.set_thumbnail(url = animeImage)
            await ctx.channel.send(embed = embedVar)
        else:
            embedVar = discord.Embed(color = discord.Colour.dark_theme())
            embedVar.add_field(name = "title" , value = f"[{animeTitle}]({animeURL})")
            embedVar.add_field(name = "MAL score" , value = animeScore)
            embedVar.add_field(name = "type" , value = animeType)
            embedVar.add_field(name = "started" , value = animeStart[0:10])
            embedVar.add_field(name = "ended" , value = animeEnd[0:10])
            embedVar.add_field(name = "no of episodes" , value = animeEpisode)
            embedVar.add_field(name = "synopsis" , value = animeSynopsis)
            embedVar.add_field(name = "rated" , value = animeRated)
            embedVar.add_field(name = "possible anime link" , value = f"[animixplay]({animixplay})\n[4anime]({anime9})")
            embedVar.set_thumbnail(url = animeImage)
            await ctx.channel.send(embed = embedVar)
    
    @ani.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(searchAni(client))

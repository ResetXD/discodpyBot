import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from animeAPI import search

class searchAni(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['ms'])
    async def mangasearch(self, ctx:Context,*,anime_name = None):
        if anime_name == None:
            await ctx.channel.send("what do i even search")
            return
        a = search.AnimeSearch("manga")
        c = await a.searchManga(anime_name)
        b = ""
        for x in range(1,6):
            d = c[x]
            b += d["title"] + "\n"
        await ctx.channel.send(b)
    
    @mangasearch.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(searchAni(client))
import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from animeAPI import search
from mangafreak import mangaPages

class searchAni(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def rm(self, ctx:Context,chapterNumber,start,end,*,anime_name = None):
        if anime_name == None:
            await ctx.channel.send("what do u even want to read")
            return
        a = search.AnimeSearch("manga")
        c = await a.searchManga(anime_name)
        c = c[0]
        animeTitle = c["title"]
        animeTitle = animeTitle.lower()
        animeTitle = animeTitle.replace(" ","-")
        animeTitle = animeTitle.replace("!","")
        animeTitle = animeTitle.replace(".","")
        animeTitle = animeTitle.replace(",","")
        a = mangaPages.MANGA_IMG()
        if start == None:
            for x in range(1,11):
                b = await a.get_page(manga_name=animeTitle,chapter=chapterNumber,page=x)
                emb = discord.Embed(title = f"{anime_name}" , color = discord.Colour.dark_theme())
                emb.set_image(url = b)
                await ctx.channel.send(embed = emb)
        if start != None and end == None:
            for x in range(int(start)//1 , (int(start)+11)//1):
                b = await a.get_page(manga_name=animeTitle,chapter=chapterNumber,page=x)
                emb = discord.Embed(title = f"{anime_name}" , color = discord.Colour.dark_theme())
                emb.set_image(url = b)
                await ctx.channel.send(embed = emb)
        else:
            for x in range(int(start)//1 , int(end)//1):
                b = await a.get_page(manga_name=animeTitle,chapter=chapterNumber,page=x)
                emb = discord.Embed(title = f"{anime_name}" , color = discord.Colour.dark_theme())
                emb.set_image(url = b)
                await ctx.channel.send(embed = emb)

    
    @rm.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(searchAni(client))
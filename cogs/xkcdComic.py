import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from xkcd import comic

class Comic(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    @commands.cooldown(rate=1,per=5)
    async def comic(self, ctx:Context):
        a = comic.Comic()
        b = await a.get_comic_url()
        embedVar = discord.Embed(title = "" , color = discord.Colour.dark_theme())
        embedVar.set_image(url=f"{b}")
        embedVar.set_footer(text="from xkcd artist")
        await ctx.send(embed=embedVar)
        return
    
    @comic.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
    
def setup(client):
    client.add_cog(Comic(client))
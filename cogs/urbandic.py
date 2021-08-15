import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from urbanAPIres import search

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['whatis','dictionary'])
    async def urban(self, ctx:Context,what):
        if what == None:
            return await ctx.channel.send("what to search?")
        a = search.Search()
        b = await a.get_search(what)
        b = b["list"][0]
        defination = b["definition"]
        permalink = b["permalink"]
        example = b["example"]
        embedVar = discord.Embed(title = "DICTIONARY" , color = discord.Colour.dark_theme())
        embedVar.add_field(name = "word",value = f"[{what}]({permalink})",inline = False)
        embedVar.add_field(name = "defination",value = f"{defination}",inline = False)
        embedVar.add_field(name = "example",value = f"{example}",inline = False)
        embedVar.set_footer(text = f"asked by {ctx.author}")
        return await ctx.channel.send(embed = embedVar)
    
    @commands.command(aliases = ['whatis1','dictionary1'])
    async def urban1(self, ctx:Context,no,what):
        if no == None or what == None:
            return await ctx.channel.send("what to search?")
        a = search.Search()
        b = await a.get_search(what)
        b = b["list"][int(no)]
        defination = b["definition"]
        permalink = b["permalink"]
        example = b["example"]
        embedVar = discord.Embed(title = "DICTIONARY" , color = discord.Colour.dark_theme() )
        embedVar.add_field(name = "word",value = f"[{what}]({permalink})",inline = False)
        embedVar.add_field(name = "defination",value = f"{defination}",inline = False)
        embedVar.add_field(name = "example",value = f"{example}",inline = False)
        embedVar.set_footer(text = f"asked by {ctx.author}")
        return await ctx.channel.send(embed = embedVar)
        
    
    @urban.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
    
    @urban1.error
    async def define1_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        
def setup(client):
    client.add_cog(Ping(client))    
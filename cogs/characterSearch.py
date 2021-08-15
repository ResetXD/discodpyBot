import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from characterSearch import character

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['char'])
    async def character(self, ctx:Context,*,name="akame"):
        a = character.char()
        b = await a.by_char_name(name)
        b = b[0]
        embedVar = discord.Embed(title = "character search",color=discord.Colour.dark_theme())
        embedVar.add_field(name="gender",value="{0}".format(b["gender"]))
        embedVar.add_field(name="name",value="{0}".format(b["name"]))
        embedVar.add_field(name="anime id",value="{0}".format(b["anime_id"]))
        embedVar.add_field(name="anime name",value="{0}".format(b["anime_name"]))
        embedVar.set_image(url="{0}".format(b["character_image"]))
        await ctx.channel.send(embed = embedVar)
        return
    
    @character.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
    ###############################################################################################

    @commands.command(aliases = ['charsearch'])
    async def charactersearch(self, ctx:Context,*,name="akame"):
        a = character.char()
        b = await a.by_char_name(name)
        embedVar = discord.Embed(title = "character search",color=discord.Colour.dark_theme())
        yy = 0
        for x in b:
            embedVar.add_field(name="gender",value="{0}".format(b["gender"]))
        await ctx.channel.send(embed = embedVar)
        return
    
    @character.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return

def setup(client):
    client.add_cog(Ping(client))
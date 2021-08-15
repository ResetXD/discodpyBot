import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Ree(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['reee'])
    @commands.cooldown(rate=1,per=5)
    async def ree(self, ctx:Context , channel : discord.TextChannel = None, *, reason = None):
        await ctx.channel.send("https://tenor.com/view/reeeeeeeeeeeeeeeeee-gif-19312523")
        return
    
    @ree.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return

def setup(client):
    client.add_cog(Ree(client))
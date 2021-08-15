import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['latency','lat'])
    async def ping(self, ctx:Context):
        await ctx.send(f"latency is {round(self.client.latency * 1000)}ms")
        return
    
    @ping.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(Ping(client))
import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Owner(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def owner(self, ctx:Context):
        await ctx.send("owner of this bot is reset#5576")  
        return
    
    @owner.error
    async def owner_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
def setup(client):
    client.add_cog(Owner(client))
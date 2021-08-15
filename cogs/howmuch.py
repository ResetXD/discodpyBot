import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class HowMuch(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    @commands.is_owner()
    async def total(self, ctx:Context):
        total = 0
        for x in self.client.guilds:
            total += x.member_count
        await ctx.channel.send(f"total number of users: {total}")
    
def setup(client):
    client.add_cog(HowMuch(client))
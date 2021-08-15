import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import random

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['holywater','bless'])
    async def bible(self, ctx:Context,who:discord.Member = None):
        if who == None:
            responses = ["<:rem_bible:861916674822111252> here is your bible and get the fuck out of here",
                         "<:rem_bible:861916674822111252> read this before saying that shit bruh",
                         "<:rem_bible:861916674822111252> fr read this cause you are opposite of this",
                         "<:rem_bible:861916674822111252> save us from this sinner"]
            return await ctx.channel.send(random.choice(responses))            
        else:
            responses = [f"{who.mention} <:rem_bible:861916674822111252> read this bible and get the fuck out of here",
                         f"{who.mention} <:rem_bible:861916674822111252> read this before saying that shit bruh",
                         f"<:rem_bible:861916674822111252> fr read this cause you are opposite of this {who.mention}",
                         f"<:rem_bible:861916674822111252> save us from this sinner {who.mention}"]
            return await ctx.channel.send(random.choice(responses))    
    
    @bible.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("there is some error but still <:rem_bible:861916674822111252>")
        return
    
def setup(client):
    client.add_cog(Ping(client))
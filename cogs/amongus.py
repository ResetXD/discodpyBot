import discord
from discord.ext.commands.cooldowns import BucketType
from discord.ext import commands
from discord.ext.commands.context import Context
from tenorAPI import getgif
import random

class Tweet(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['amoungus','au'])
    @commands.cooldown(rate=1,per=1,type=BucketType.user)
    async def amogus(self,ctx:Context):
        a = getgif.GetGif()
        b = await a.amongusGIF() 
        c = random.choice(b)
        await ctx.channel.send(c["url"])
        return

    @amogus.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send(error)
        return
    
def setup(client):
    client.add_cog(Tweet(client))
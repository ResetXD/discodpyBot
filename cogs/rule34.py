import discord
from discord.ext.commands.cooldowns import BucketType
from discord.ext import commands
from discord.ext.commands.context import Context
import random
from r3PI import media

class Tweet(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['r34','34'])
    @commands.cooldown(rate=1,per=2,type=BucketType.user)
    async def rule34(self,ctx:Context,tag="re:zero"):
        if ctx.channel.is_nsfw():
            a = media.GetGif()
            b = await a.get_(tag)
            c = random.choice(b)
            await ctx.channel.send(c["file_url"])
            return
        else:
            await ctx.channel.send("this isnt a no no channel")
            return

    @rule34.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(Tweet(client))
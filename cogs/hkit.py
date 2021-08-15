import discord
from discord.ext.commands.cooldowns import BucketType
from discord.ext import commands
from discord.ext.commands.context import Context
from nekobotAPI import imageGrabber

class Hen(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    @commands.cooldown(rate=1,per=5,type=BucketType.user)
    async def hkitsune(self, ctx:Context):
        if ctx.channel.is_nsfw():
            a = imageGrabber.imageGrabber()
            b = await a.get_image(imgType="hkitsune")
            await ctx.channel.send(b)
            return
        else:
            await ctx.channel.send("this isnt a no no channel")
            return
    
    @hkitsune.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(Hen(client))
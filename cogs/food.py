import discord
from discord.ext.commands.cooldowns import BucketType
from discord.ext import commands
from discord.ext.commands.context import Context
from nekobotAPI import imageGrabber

class Hen(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    @commands.cooldown(rate=1,per=2,type=BucketType.user)
    async def food(self, ctx:Context):
        a = imageGrabber.imageGrabber()
        b = await a.get_image(imgType="food")
        await ctx.channel.send(b)
        return

    @food.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    

    @commands.command()
    @commands.cooldown(rate=1,per=2,type=BucketType.user)
    async def coffee(self, ctx:Context):
        a = imageGrabber.imageGrabber()
        b = await a.get_image(imgType="coffee")
        await ctx.channel.send(b)
        return

    @coffee.error
    async def coffee_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
    @commands.command(aliases = ["omg"])
    @commands.cooldown(rate=1,per=2,type=BucketType.user)
    async def gah(self, ctx:Context):
        a = imageGrabber.imageGrabber()
        b = await a.get_image(imgType="gah")
        await ctx.channel.send(b)
        return

    @gah.error
    async def gah_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
    @commands.command()
    @commands.cooldown(rate=1,per=2,type=BucketType.user)
    async def kannaa(self, ctx:Context):
        a = imageGrabber.imageGrabber()
        b = await a.get_image(imgType="kanna")
        await ctx.channel.send(b)
        return

    @kannaa.error
    async def kanna_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(Hen(client))
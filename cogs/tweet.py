import discord
from discord.ext.commands.cooldowns import BucketType
from discord.ext import commands
from discord.ext.commands.context import Context
from nekobotAPI import imageGrabber

class Tweet(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['twitter'])
    @commands.cooldown(rate=1,per=5,type=BucketType.user)
    async def tweet(self, ctx:Context,who:discord.Member = None,*,text=None):
        if who == None:
            await ctx.channel.send("no user provided")
        try:
            c = imageGrabber.imageGrabber()
            msg = await ctx.channel.send("wait a damn min")
            d = await c.get_imagegen_tweet(imgType="tweet",text=text,username=who)
            await msg.edit(content = d)
        except:
            c = imageGrabber.imageGrabber()
            msg = await ctx.channel.send("wait a damn min")
            d = await c.get_imagegen_tweet(imgType="tweet",text=text,username=who)
            await msg.edit(content = d)

    
    @tweet.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(Tweet(client))
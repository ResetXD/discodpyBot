import discord
from discord.ext.commands.cooldowns import BucketType
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.member import Member
from nekobotAPI import imageGrabber

class Magik(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    @commands.cooldown(rate=1,per=10,type=BucketType.user)
    async def magik(self, ctx:Context,who:discord.Member = None):
        if who == None:
            user = ctx.message.author
            pfp = str(user.avatar_url_as(format="jpg"))
        else:
            pfp = str(who.avatar_url_as(format="jpg"))
        a = pfp.split("https/")
        try:
            b = "https://"+a[1]
            c = imageGrabber.imageGrabber()
            msg = await ctx.channel.send("wait a damn min")
            d = await c.get_imagegen(imgType="magik",image=b)
            await msg.edit(content = d)
        except:
            b = a[0]
            c = imageGrabber.imageGrabber()
            msg = await ctx.channel.send("wait a damn min")
            d = await c.get_imagegen(imgType="magik",image=b)
            await msg.edit(content = d)

    
    @magik.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(Magik(client))
import discord
from discord.ext.commands.cooldowns import BucketType
from discord.ext import commands
from discord.ext.commands.context import Context
from nekobotAPI import imageGrabber

class Neko(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['catgirl'])
    @commands.cooldown(rate=1,per=5,type=BucketType.user)
    async def neko(self, ctx:Context):
        a = imageGrabber.imageGrabber()
        b = await a.get_image(imgType="neko")
        await ctx.channel.send(b)
    
    @neko.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return

def setup(client):
    client.add_cog(Neko(client))
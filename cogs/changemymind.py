import discord
from discord.ext.commands.cooldowns import BucketType
from discord.ext import commands
from discord.ext.commands.context import Context
from nekobotAPI import imageGrabber

class loli(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases=['change'])
    @commands.cooldown(rate=1,per=15,type=BucketType.user)
    async def changemymind(self, ctx:Context,*,text = None):
        if text == None:
          text = "giv sauce"
        try:
            c = imageGrabber.imageGrabber()
            msg = await ctx.channel.send("wait a damn min")
            d = await c.get_imagegen_kanna(imgType="changemymind",text=text)
            await msg.edit(content = d)
        except:
            c = imageGrabber.imageGrabber()
            msg = await ctx.channel.send("wait a damn min")
            d = await c.get_imagegen_kanna(imgType="changemymind",text=text)
            await msg.edit(content = d)

    
    @changemymind.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(loli(client))
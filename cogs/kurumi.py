import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import base64
from imagegeneration import getImage
import random

class Ping(commands.Cog):

    def __init__(self,client,kurumi):
        self.client = client
        self.kurumi = kurumi
    
    @commands.command()
    async def addk(self, ctx:Context):
        for attac in ctx.message.attachments:
            a = attac.url
            ab = getImage.getImage()
            b = await ab.get_image_byURL(a)
            with open("imageByUrl.jpg", "rb") as image2string:
                converted_string = base64.b64encode(image2string.read())
                abc = await self.kurumi.insert_one({"encoded":converted_string})
        return
    
    @addk.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
    @commands.command()
    async def kurumi(self, ctx:Context):
        msg = await ctx.channel.send("ok <:kurumi_what:865487594892165130>")
        acc = self.kurumi.find()
        acc = await acc.to_list(length=100)
        x = random.choice(acc)
        decodeit = open('okokok.jpg', 'wb')
        decodeit.write(base64.b64decode(x["encoded"]))
        decodeit.close()
        with open('okokok.jpg', 'rb') as f:
            picture = discord.File(f)
            await ctx.channel.send(file=picture)
            await msg.delete()
    
    @kurumi.error
    async def kurumi_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(Ping(client,client.kurumi))
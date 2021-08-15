import asyncio

import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from nekobotAPI import imageGrabber


class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def autohentai(self, ctx:Context,channel:discord.TextChannel = None):
        if channel == None:
            channel = ctx.channel
        if ctx.channel.is_nsfw():
            channel = self.client.get_channel(int(channel.id))
            while True:
                a = imageGrabber.imageGrabber()
                b = await a.get_image(imgType="hentai")
                await ctx.channel.send(b)
                await asyncio.sleep(60)
        else:
          return await ctx.channel.send("this isnt a no no channel")
    
    @autohentai.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(Ping(client))

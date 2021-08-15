import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import asyncio
import concurrent
from googletrans import Translator

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client
        self.pool = concurrent.futures.ThreadPoolExecutor()
        self.loop = asyncio.get_event_loop()
        self.result = ""

    @commands.command()
    async def translate(self, ctx:Context,lanuage,*text):
        msg = await ctx.channel.send("this may take time depending on the api speed") 
        await msg.edit("result")
        return
    
    @translate.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(Ping(client))
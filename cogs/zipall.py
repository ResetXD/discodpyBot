import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from imagegeneration import getImage
import aiofiles
import aiohttp
import os
import shutil

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def zip(self, ctx:Context,what):
        if what == "emoji":
            msg = await ctx.channel.send("may take time depeding upon the number of emoji in the server")
            for x in ctx.guild.emojis:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"{x.url}") as resp:
                        if resp.status == 200:
                            f = await aiofiles.open(f'./emojiDB/{x.name}.jpg', mode='wb')
                            await f.write(await resp.read())
                            await f.close()
            
            shutil.make_archive(f"{ctx.guild}-emoji","zip","emojiDB")
            with open(f'{ctx.guild}-emoji.zip', 'rb') as f:
                ziip = discord.File(f)
                await ctx.channel.send(file=ziip)
            await msg.delete()
            os.remove(f"{ctx.guild}-emoji.zip")
            shutil.rmtree(f"emojiDB")
            os.mkdir("emojiDB")
            await ctx.channel.send("done")
                
        return
    
    # @zip.error
    # async def define_error(self, ctx:Context ,error):
    #     await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
    #     return
    
def setup(client):
    client.add_cog(Ping(client))
import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import random

from discord.utils import get
from wallpaperAPI import getWallpaper

class account(commands.Cog):

    def __init__(self,client,economydb):
        self.client = client
        self.wallpaperdb = economydb
        
    @commands.command(aliases = ["bg","wallpaper","wall"])
    async def background(self, ctx:Context,*,what = "tokisaki kurumi"):
        a = getWallpaper.getWallpaper()
        b = await a.get_wallpaper_by_tag(what)
        embedVar = discord.Embed(title = "" , color = discord.Colour.dark_theme())
        embedVar.set_image(url=random.choice(b)["path"])
        await ctx.channel.send(embed = embedVar)
    
def setup(client):
    client.add_cog(account(client,client.wallpaperdb))
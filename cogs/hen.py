import discord
from discord.ext.commands.cooldowns import BucketType
from discord.ext import commands
from discord.ext.commands.context import Context
from nekobotAPI import imageGrabber
from danbooru import getImage
import random

class Hen(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['Hentai'])
    @commands.cooldown(rate=1,per=2,type=BucketType.user)
    async def hentai(self, ctx:Context):
        if ctx.channel.is_nsfw():
            a = imageGrabber.imageGrabber()
            b = await a.get_image(imgType="hentai")
            embedVar = discord.Embed(title = "" , color = discord.Colour.dark_theme())
            embedVar.set_image(url=b)
            await ctx.channel.send(embed = embedVar)
            return
        else:
            await ctx.channel.send("this isnt a no no channel")
            return
    @hentai.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
    ###############################################################################################

    @commands.command(aliases = ["randomdanbooru","randdanbooru"])
    @commands.cooldown(rate=1,per=2,type=BucketType.user)
    async def randdan(self, ctx:Context):
        if ctx.channel.is_nsfw():
            a = getImage.getIMAGE()
            b = await a.get_random()
            embedVar = discord.Embed(title = "" , color = discord.Colour.dark_theme())
            embedVar.set_image(url=b)
            await ctx.channel.send(embed = embedVar)
            return
        else:
            await ctx.channel.send("this isnt a no no channel")
            return
    @randdan.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
    ###########################################################################################

    @commands.command(aliases = ["danbooru"])
    @commands.cooldown(rate=1,per=2,type=BucketType.user)
    async def dan(self, ctx:Context,*,tag = None):
        if tag == None:
            return await ctx.channel.send("what to search?")
        if ctx.channel.is_nsfw():
            tag = tag.replace(" ","_")
            a = getImage.getIMAGE()
            b = await a.get_by_tag(tag)
            b = random.choice(b)
            embedVar = discord.Embed(title = "" , color = discord.Colour.dark_theme())
            embedVar.set_image(url=b["file_url"])
            await ctx.channel.send(embed = embedVar)
            return
        else:
            await ctx.channel.send("this isnt a no no channel")
            return
    @dan.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
    #####################################################################################################
    
    @commands.command(aliases = ["dansearch","ds"])
    @commands.cooldown(rate=1,per=2,type=BucketType.user)
    async def searchdan(self, ctx:Context,*,tag = None):
        if tag == None:
            return await ctx.channel.send("what to search?")
        if ctx.channel.is_nsfw():
            tag = tag.replace(" ","_")
            a = getImage.getIMAGE()
            b = await a.search_tag(tag)
            aaa = ""
            for x in b:
                aaa += x["name"].replace("_","\_") + "\n"
            await ctx.channel.send(f"available tags:\n{aaa}")
            return
        else:
            await ctx.channel.send("this isnt a no no channel")
            return
    @searchdan.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return


def setup(client):
    client.add_cog(Hen(client))
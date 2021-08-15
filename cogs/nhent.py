import discord
from discord.ext.commands.cooldowns import BucketType
from discord.ext import commands
from discord.ext.commands.context import Context
from nbook import nhen
from nbook import nhenIMG

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ["rh"])
    async def readnhentai(self,ctx:Context,id=None,start=None,end=None):
        a = nhenIMG.NHEN_IMG()
        if ctx.channel.is_nsfw():
            if id == None:
                return await ctx.channel.send("media_id?")
            elif start == None:
                for x in range(1,11):
                    b = await a.get_page(id=id,page=x)
                    await ctx.channel.send(b)
            elif start != None and end == None:
                for x in range(int(start)//1 , (int(start)+11)//1):
                    b = await a.get_page(id=id,page=x)
                    await ctx.channel.send(b)
            else:
                for x in range(int(start)//1 , int(end)//1):
                    b = await a.get_page(id=id,page=x)
                    await ctx.channel.send(b)

        else:
            return await ctx.channel.send("this isnt a no no channel")
    
    @commands.command()
    async def nhentai(self, ctx:Context,id = None):
        if ctx.channel.is_nsfw():
            if id == None:
                return await ctx.channel.send("id?")
            a = nhen.NHEN_json()
            b = await a.get_rawJSON(id=id)
            title = b["title"]
            title = title["pretty"]
            c = b["media_id"]
            d = nhenIMG.NHEN_IMG()
            d = await d.get_page(id=c,page="1")
            tag = b["tags"]
            e = ""
            num = b["num_pages"]
            for x in tag:
                e += x["name"]+","

            embedVar = discord.Embed(title = f"{title}", color = discord.Colour.dark_theme())
            embedVar.add_field(name = "link" , value = f"[link to nhentai.net](https://nhentai.net/g/{id})",inline = False)
            embedVar.add_field(name = "media_id (important if are reading the book here)" , value = f"{c}",inline = False)
            embedVar.add_field(name = "tags" , value = f"{e}nhentai",inline = False)
            embedVar.add_field(name = "number of pages" , value = f"{num}",inline = False)
            embedVar.set_thumbnail(url = d)
            await ctx.channel.send(embed = embedVar)
            return
        else:
            return await ctx.channel.send("this isnt a no no channel")
    
    @nhentai.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(Ping(client))
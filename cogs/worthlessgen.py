import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from memegeneration import worthless
from memegeneration import spongebob
from memegeneration import ew
from memegeneration import hellno
from memegeneration import face
from memegeneration import yeet

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def worthless(self, ctx:Context,*,text="you are worthless"):
        a = worthless.Worthless()
        msg = await ctx.channel.send("wait a damn min")
        b = a.worthless(text)
        with open('worthsend.jpg', 'rb') as f:
            picture = discord.File(f)
            await msg.delete()
            await ctx.channel.send(file=picture)
        return
    
    @worthless.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        await ctx.channel.send("if its an error kindly report it to the dev ;)")
        return
    
    @commands.command()
    async def spongebob(self, ctx:Context,*,text="you are worthless"):
        a = spongebob.spongebob()
        msg = await ctx.channel.send("wait a damn min")
        b = a.sp(text)
        with open('sponge.jpg', 'rb') as f:
            picture = discord.File(f)
            await msg.delete()
            await ctx.channel.send(file=picture)
        return
    
    @spongebob.error
    async def spongebob_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        await ctx.channel.send("if its an error kindly report it to the dev ;)")
        return
    

    @commands.command()
    async def ew(self, ctx:Context,who:discord.Member):
        a = ew.ew()
        msg = await ctx.channel.send("wait a damn min")
        av = who.avatar_url_as(format = "png")
        b = await a.get_ew_img(str(av))
        with open('ewtest.png', 'rb') as f:
            picture = discord.File(f)
            await msg.delete()
            await ctx.channel.send(file=picture)
        return
    
    @ew.error
    async def ew_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        await ctx.channel.send("if its an error kindly report it to the dev ;)")
        return
    
    @commands.command()
    async def snap(self, ctx:Context,who:discord.Member):
        a = hellno.hellno()
        msg = await ctx.channel.send("wait a damn min")
        av = who.avatar_url_as(format = "png")
        b = await a.get_hell_no(str(av))
        with open('ewtest.png', 'rb') as f:
            picture = discord.File(f)
            await msg.delete()
            await ctx.channel.send(file=picture)
        return
    
    @snap.error
    async def snap_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        await ctx.channel.send("if its an error kindly report it to the dev ;)")
        return
    
    @commands.command()
    async def face(self, ctx:Context,who:discord.Member):
        a = face.face()
        msg = await ctx.channel.send("wait a damn min")
        av = who.avatar_url_as(format = "jpg")
        b = await a.get_face(str(av))
        with open('ewtest.png', 'rb') as f:
            picture = discord.File(f)
            await msg.delete()
            await ctx.channel.send(file=picture)
        return
    
    @face.error
    async def face_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        await ctx.channel.send("if its an error kindly report it to the dev ;)")
        return
    

    @commands.command()
    async def yeet(self, ctx:Context,who:discord.Member):
        a = yeet.yeet()
        msg = await ctx.channel.send("wait a damn min")
        av = who.avatar_url_as(format = "jpg")
        b = await a.get_yeet(str(av))
        with open('ewtest.png', 'rb') as f:
            picture = discord.File(f)
            await msg.delete()
            await ctx.channel.send(file=picture)
        return
    
    @yeet.error
    async def yeet_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        await ctx.channel.send("if its an error kindly report it to the dev ;)")
        return
    
def setup(client):
    client.add_cog(Ping(client))
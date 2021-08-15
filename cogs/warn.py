from logging import warn
import discord
from discord import embeds
from discord.ext import commands
from discord.ext.commands.context import Context

class Warn(commands.Cog):

    def __init__(self,client,collection):
        self.client = client
        self.coll = collection
    
    @commands.command(aliases = ['w','w+'])
    @commands.has_permissions(kick_members = True)
    async def warn(self, ctx:Context,who: discord.Member):
        primary_key = str(ctx.guild.id) + str(who.id)
        try:
            case = await self.coll.find_one({'_id': str(primary_key)})
            warns = int(case['warns'])
            warns += 1
            await self.coll.replace_one({'_id': str(primary_key)},{'_id': str(primary_key),"warns":warns}, True)
            varembed = discord.Embed(title = "user warned" , color = discord.Colour.dark_theme())
            varembed.add_field(name = f"warned {who} now they have {warns} warns",value = f"warned by {ctx.author}",inline = False)
            varembed.set_thumbnail(url=who.avatar_url)
            varembed.set_footer(text= f"warned by {ctx.author}",icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed = varembed)

        except:
            await self.coll.replace_one({'_id': str(primary_key)},{'_id': str(primary_key),"warns":"1"}, True)
            varembed = discord.Embed(title = "user warned" , color = discord.Colour.dark_theme())
            varembed.add_field(name = f"warned {who} now they have there first warn",value = f"warned by {ctx.author}",inline = False)
            varembed.set_thumbnail(url=who.avatar_url)
            varembed.set_footer(text= f"warned by {ctx.author}",icon_url=ctx.author.avatar_url)
            await ctx.channel.send(embed = varembed)

    @warn.error
    async def warn_error(self, ctx:Context ,error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send("<:kurumi_ara_ara:865856459383898113>")
            await ctx.send("either you or i dont have the permission to do that(kick_members)")
            return
        else:
            await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))



    @commands.command(aliases = ['rw','w-'])
    @commands.has_permissions(kick_members = True)
    async def removewarn(self, ctx:Context,who: discord.Member):
        primary_key = str(ctx.guild.id) + str(who.id)
        try:
            case = await self.coll.find_one({'_id': str(primary_key)})
            warns = int(case['warns'])
            warns -= 1
            await self.coll.replace_one({'_id': str(primary_key)},{'_id': str(primary_key),"warns":warns}, True)
            varembed = discord.Embed(title = "user warned" , color = discord.Colour.dark_theme())
            varembed.add_field(name = f"warned {who} now they have {warns} warns",value = f"warned by {ctx.author}",inline = False)
            varembed.set_footer(text= f"remove warn by {ctx.author}",icon_url=ctx.author.avatar_url)
            varembed.set_thumbnail(url=who.avatar_url)
            await ctx.channel.send(embed = varembed)
        except:
            await self.coll.replace_one({'_id': str(primary_key)},{'_id': str(primary_key),"warns":"0"}, True)
            varembed = discord.Embed(title = "user warned" , color = discord.Colour.dark_theme())
            varembed.add_field(name = f"warned {who} now they have zero warn",value = f"warned by {ctx.author}",inline = False)
            varembed.set_footer(text= f"removed warn by {ctx.author}",icon_url=ctx.author.avatar_url)
            varembed.set_thumbnail(url=who.avatar_url)
            await ctx.channel.send(embed = varembed)

    @removewarn.error
    async def nickname_error(self, ctx:Context ,error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> ")
            await ctx.send("either you or i dont have the permission to do that(kick_members)")
            return
        else:
            await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))

def setup(client):
    client.add_cog(Warn(client,client.warnCol))
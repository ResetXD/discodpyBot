import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['invitebg'])
    async def splash(self, ctx:Context):
        banner = ctx.guild.splash_url
        await ctx.channel.send(banner)
        return
    
    @commands.command(aliases = ['serverbanner'])
    async def banner(self, ctx:Context):
        banner = ctx.guild.banner_url
        await ctx.channel.send(banner)
        return
    
    @splash.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("server doesnt have a splash")
        return
    
    @banner.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("server doesnt have a banner")
        return
    
def setup(client):
    client.add_cog(Ping(client))
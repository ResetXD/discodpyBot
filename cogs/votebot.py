import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def vote(self, ctx:Context):
        invite_link = "https://top.gg/bot/832173660952985610/vote"
        embedVar = discord.Embed(title = "" , color = discord.Colour.dark_theme())
        embedVar.add_field(name = "vote here" , value = f"[click me]({invite_link})")
        await ctx.send(embed = embedVar)
    
    @vote.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("how tf did u break this command")
        return
    
def setup(client):
    client.add_cog(Ping(client))
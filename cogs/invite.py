import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['server',"support"])
    async def invite(self, ctx:Context):
        invite_link = "https://discord.com/api/oauth2/authorize?client_id=832173660952985610&permissions=8&scope=bot"
        server_link = "https://discord.gg/PFxuf3Vvwj"
        embedVar = discord.Embed(title = "" , color = discord.Colour.dark_theme())
        embedVar.add_field(name = "invite me" , value = f"[click me]({invite_link})")
        embedVar.add_field(name = "join my support server" , value = f"[click me]({server_link})")
        embedVar.add_field(name = "also join this anime server" , value = f"[click me](https://discord.gg/indiananime)")
        await ctx.send(embed = embedVar)
    
    @invite.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("how tf did u break this command")
        return
    
def setup(client):
    client.add_cog(Ping(client))
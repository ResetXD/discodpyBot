import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['message'])
    @commands.has_permissions(administrator = True)
    async def dm(self, ctx:Context,who: discord.User = None,*,message=None):
        if who == None:
            return await ctx.channel.send("who?")
        elif message == None:
            return await ctx.channel.send("message?")
        else:
            direct_dm = await who.create_dm()
            message = message
            await direct_dm.send(content=message)
            await ctx.channel.send(f"messaged {who.name}")
            chan = self.client.get_channel(862571563819204608)
            embedVar = discord.Embed(title = "dm log" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = ctx.author.avatar_url)
            embedVar.add_field(name = "message",value = f"{message}",inline = False)
            embedVar.add_field(name = "who to whom",value = f"{ctx.author} to {who}",inline = False)
            await chan.send(embed = embedVar)
            return

    
    @dm.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(Ping(client))
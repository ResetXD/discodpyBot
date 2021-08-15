import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class DelChannel(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['dc','DC','DELETECHANNEL'])
    @commands.has_permissions(manage_channels = True )
    async def deletechannel(self, ctx:Context , channel : discord.TextChannel = None, *, reason = None):
        if channel == None:
            await ctx.send("which one?")
        else:    
            try:
                await channel.delete(reason = reason)
                await ctx.send("done")
            except:
                await ctx.send("something went wrong")
        return

    @deletechannel.error
    async def purge_error(self, ctx:Context ,error):
        if isinstance(error, commands.MissingPermissions):
            embedVar = discord.Embed(color = discord.Colour.dark_theme())
            embedVar.add_field(name = "deleteChannel command" , value = "either you or i dont have the permission to do that(manage_channels)",inline = False)
            await ctx.channel.send(embed = embedVar)
        else:
            await ctx.channel.send("looks like a error join support server to inform the dev to improve this bot https://discord.gg/PFxuf3Vvwj")
        return

def setup(client):
    client.add_cog(DelChannel(client))
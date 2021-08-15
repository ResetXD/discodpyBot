import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class CreChannel(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['cc','CC','CREATECHANNEL'])
    @commands.has_permissions(manage_channels = True )
    async def createchannel(self, ctx:Context , channel : discord.TextChannel , * ,cn = None ):
        if cn == None:
            await channel.clone(name = "general")
            await ctx.send("done")
        else:    
            await channel.clone(name = cn)
            await ctx.send("done")
        return

    @createchannel.error
    async def purge_error(self, ctx:Context ,error):
        if isinstance(error, commands.MissingPermissions):
            embedVar = discord.Embed(color = discord.Colour.dark_theme())
            embedVar.add_field(name = "createChannel command" , value = "either you or i dont have the permission to do that(manage_channels)",inline = False)
            await ctx.channel.send(embed = embedVar)
        else:
            await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    

def setup(client):
    client.add_cog(CreChannel(client))
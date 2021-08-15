import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class GiveRole(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['giverole','addrole'])
    @commands.has_permissions(manage_roles = True)
    async def gr(self,ctx:Context,role: discord.Role,member: discord.Member = None):
        if member == None:
            await ctx.channel.send("to who?")
        await member.add_roles(role)
        await ctx.channel.send(f'gave {member} {role}')
        return
    
    @gr.error
    async def gr_error(self, ctx:Context ,error):
        if isinstance(error, commands.MissingPermissions):
            embedVar = discord.Embed(color = discord.Colour.dark_theme())
            embedVar.add_field(name = "giverole command" , value = "either you or i dont have the permission to do that(manage_roles)",inline = False)
            await ctx.channel.send(embed = embedVar)
        else:
            await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(GiveRole(client))
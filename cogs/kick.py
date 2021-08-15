import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Kick(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self,ctx: Context, member: discord.Member, *, reason=None):
        embedVar = discord.Embed(color = discord.Colour.dark_theme())
        embedVar.add_field(name = "kicked" , value = "kicked the user from the guild",inline = False)
        embedVar.set_footer(text = "reason = {}".format(reason))
        await member.kick(reason=reason)
        await ctx.channel.send(embed = embedVar)
        return
    
    @kick.error
    async def nickname_error(self, ctx:Context ,error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send("either you or i dont have the permission to do that(kick_members)")
            return
        else:
            await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
            return
def setup(client):
    client.add_cog(Kick(client))
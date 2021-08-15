# @client.command(pass_context=True)
import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Nickname(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(aliases = ['nick'])
    @commands.has_permissions(manage_nicknames = True)
    async def nickname(self, ctx : Context, member: discord.Member, *, nick):
        await member.edit(nick=nick)
        await ctx.send(f'{member} \'s nickname have been changed ')
        return
    
    @nickname.error
    async def nickname_error(self, ctx:Context ,error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("either you or i dont have the permission to do that(manage_nicknames)")
            return
        else:
            await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
            return

def setup(client):
    client.add_cog(Nickname(client))
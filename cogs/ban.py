import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Ban(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(aliases = ['removeunban','REMOVEUNBAN','BAN'])
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx:Context,who:discord.Member = None, *,reason = None):
        if who == None:
            embedVar = discord.Embed(color = discord.Colour.dark_theme())
            embedVar.add_field(name = "ban command" , value = "ping or use the id",inline = False)
            await ctx.channel.send(embed = embedVar)
        else:
            embedVar = discord.Embed(color = discord.Colour.dark_theme())
            embedVar.add_field(name = "baned" , value = "banned the user from the guild",inline = False)
            embedVar.set_footer(text = "to unban use \"res unban <user ID>\"")
            await who.ban(reason = reason)
            await ctx.channel.send(embed = embedVar)
        return

    @ban.error
    async def ban_error(self, ctx:Context ,error):
        if isinstance(error, commands.MissingPermissions):
            embedVar = discord.Embed(color = discord.Colour.dark_theme())
            embedVar.add_field(name = "baned command" , value = "either you or i dont have the permission to do that(ban_members)",inline = False)
            await ctx.channel.send(embed = embedVar)
        else:
            await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return

def setup(client):
    client.add_cog(Ban(client))
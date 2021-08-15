import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class UnBan(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(aliases = ['removeban'])
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx:Context,who = None, *,reason = None):
        if who == None:
            embedVar = discord.Embed(color = discord.Colour.dark_theme())
            embedVar.add_field(name = "unban command" , value = "use the id",inline = False)
            await ctx.channel.send(embed = embedVar)
            return
        else:
            user = await self.client.fetch_user(who)
            await ctx.guild.unban(user)
            embedVar = discord.Embed(color = discord.Colour.dark_theme())
            embedVar.add_field(name = "unbaned" , value = "unbanned the user from the guild",inline = False)
            embedVar.set_footer(text = "to ban again use \"res ban <user ID>\"") 
            await ctx.channel.send(embed = embedVar)
            return

    @unban.error
    async def purge_error(self, ctx:Context ,error):
        if isinstance(error, commands.MissingPermissions):
            embedVar = discord.Embed(color = discord.Colour.gold())
            embedVar.add_field(name = "unbaned command" , value = "either you or i dont have the permission to do that(ban_members)",inline = False)
            await ctx.channel.send(embed = embedVar)
            return
        else:
            return await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))

def setup(client):
    client.add_cog(UnBan(client))
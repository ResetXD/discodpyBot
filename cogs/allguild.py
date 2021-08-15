import discord
from discord.ext import commands
from discord.ext.commands.context import Context


class ListGuild(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['lg','guilds'])
    @commands.is_owner()
    async def listguild(self,ctx):
        servers = self.client.guilds
        description_info = ""
        
        for guild in servers:
            ids = guild.id
            description_info += "**" + str(guild.name) + "**\n" + str(guild.member_count) + " members\n"+"**ID: **"+ str(ids)

            embed = discord.Embed(description = description_info, colour=discord.Colour.gold())
            embed.set_thumbnail(url=guild.icon_url)
            await ctx.send(embed=embed)
            description_info = ""
        return


def setup(client):
    client.add_cog(ListGuild(client))

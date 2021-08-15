import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class guildInvite(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    @commands.is_owner()
    async def gi(self,ctx:Context):
        servers = self.client.guilds
        for guild in servers:
            channel = guild.system_channel
            if channel == None:
                pass
            else:
                invitelink = await channel.create_invite(max_uses=1)
                await ctx.channel.send(invitelink)

def setup(client):
    client.add_cog(guildInvite(client))
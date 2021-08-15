import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class ServerInfo(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['si','whereami'])
    async def serverinfo(self, ctx:Context):
        server = ctx.message.guild
        channel_count = len([x for x in server.channels if type(x) == discord.channel.TextChannel])
        role_count = len(server.roles)
        emoji_count = len(server.emojis)
        embedVar = discord.Embed(title = "server info" , color = discord.Colour.dark_theme())
        embedVar.add_field(name = "server Name" , value = f"{server.name}",inline = False)
        embedVar.add_field(name = "server ID" , value = f"{server.id}",inline = False)
        embedVar.add_field(name='Owner ID', value=server.owner_id, inline= False)
        embedVar.add_field(name='server region', value=server.region)
        embedVar.add_field(name='Members Count', value= server.member_count, inline = False)
        embedVar.add_field(name='textChannel Count', value= channel_count, inline = False)
        embedVar.add_field(name='Number of roles', value=str(role_count) , inline = False)
        embedVar.add_field(name='Number of emojie', value=str(emoji_count) , inline = False)
        embedVar.add_field(name='Created on', value=server.created_at)
        embedVar.set_thumbnail(url = server.icon_url)
        await ctx.channel.send(embed = embedVar)
        return

    @commands.command(aliases = ["listroles"])
    async def roles(self,ctx : Context):
        server = ctx.message.guild
        embedVar = discord.Embed(title = "role info" , color = discord.Colour.gold())
        des = "lowest to highest \n"
        for rol in server.roles:
            des += rol.mention + "\n" 

        embedVar.add_field(name = "roles" , value = des , inline = False)
        await ctx.channel.send(embed = embedVar)
        return


def setup(client):
    client.add_cog(ServerInfo(client))
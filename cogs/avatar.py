import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Avatar(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(aliases = ['av','avatar',"PFP",'AV','AVATAR'])
    async def pfp(self,ctx:Context , who:discord.Member = None):
        if who == None:
            user = ctx.message.author
            pfp = user.avatar_url
            emberVar = discord.Embed(color = discord.Colour.dark_theme())
            emberVar.set_image(url = pfp)
            await ctx.channel.send(embed = emberVar)
        else:
            pfp = who.avatar_url
            emberVar = discord.Embed(color = discord.Colour.dark_theme())
            emberVar.set_image(url = pfp)
            await ctx.channel.send(embed = emberVar)
        return
    
    @pfp.error
    async def pfp_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
        

def setup(client):
    client.add_cog(Avatar(client))
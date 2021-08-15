import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Purge(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(aliases = ['purge','clean','vanish','bulkremove'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx: Context , howMuch = 2,who:discord.Member=None):
        if not who == None:
            if who == ctx.author:
                howMuch += 1
            messages = await ctx.channel.history(limit=100).flatten()
            for x in messages:
                if howMuch <= 0:
                    return
                if x.author.id == who.id:
                    await x.delete()
                    howMuch -= 1
        else:
            await ctx.channel.purge(limit = howMuch + 1)
        return

    @clear.error
    async def purge_error(self,ctx:Context ,error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send("<:kurumi_ara_ara:865856459383898113>")
            await ctx.send("either you or i dont have the permission to do that(manage_messages)")
            return
        else:
            await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
    

def setup(client):
    client.add_cog(Purge(client))
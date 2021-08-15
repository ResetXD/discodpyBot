#never intended to add

import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class bj(commands.Cog):

    def __init__(self,client,economydb):
        self.client = client
        self.bj = economydb
        self.card = ["A","K","Q","J","2","3","4","5","6","7","8","9","10"]
    
    @commands.command(aliases = ['bj'])
    async def blackjack(self, ctx:Context, howmuch = None):
        try:
            playStatus = await self.bj.find_one({'_id': str(ctx.author.id)})
            if playStatus == None:
                if howmuch == None:
                    await ctx.channel.send("ye ye poor bet some moni next time")
                    return
                else:
                    await ctx.channel.send("place where your game start")
            else:
                if howmuch == "hit" or howmuch == "h":
                    pass
                elif howmuch == "stand" or howmuch == "s":
                    pass
                else:
                    await ctx.channel.send("sureeee sure sure sureeeeeee")
                    return
        except:
            pass
        
        
    
def setup(client):
    client.add_cog(bj(client,client.bj))
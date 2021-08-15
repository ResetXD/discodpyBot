import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import random

class Roll(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['rand','random', 'randomint'])
    async def roll(self, ctx:Context ,start = None, end = None):
        if start != None and end == None:
            try:
                number = random.randint(0,int(start))
                await ctx.channel.send(str(number))
                return
            except:
                await ctx.channel.send("got an error on my side cause maybe the number u input isnt acutally a number")
                return
        
        elif start != None and end != None:
            try:
                number = random.randint(int(start),int(end))
                await ctx.channel.send(str(number))
                return
            except:
                await ctx.channel.send("got an error on my side cause maybe the number u input isnt acutally a number")
                return
        else:
                number = random.randint(0,100)
                await ctx.channel.send(str(number))
                return


    @roll.error
    async def roll_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return


def setup(client):
    client.add_cog(Roll(client))
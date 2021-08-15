import discord
from discord.ext.commands.cooldowns import BucketType
from discord.ext import commands
from discord.ext.commands.context import Context
import random


class Roll(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['pick','po','whichone','PO','WHICHONE','PICK','CHOICE'])
    async def choice(self, ctx:Context ,*,choose = None):
        if choose == None:
            await ctx.channel.send("***there is nothing to choose from***")
        else:
            a = choose.split(" ")
            b = random.choice(a)
            await ctx.channel.send(b)
        return
    
    @choice.error
    async def choice_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
        
def setup(client):
    client.add_cog(Roll(client))
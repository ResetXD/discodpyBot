import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import random

class Rps(commands.Cog):

    def __init__(self,client):
        self.client = client
        self.choice = ['rock' , 'paper' , 'scissor']
    
    @commands.command(aliases = ['rockpaperscissorshoot'])
    async def rps(self, ctx:Context , answer = None):
        computerAnswer = random.choice(self.choice)
        if(computerAnswer == "rock" and (answer == "rock")):
            await ctx.channel.send("its a tie")
        elif(computerAnswer == "paper" and answer == "paper"):
            await ctx.channel.send("its a tie")
        elif(computerAnswer == "scissor" and answer == "scissor"):
            await ctx.channel.send("its a tie")      
        elif(computerAnswer == "rock" and answer == "paper"):
            await ctx.channel.send("player won")
        elif(computerAnswer == "scissor" and answer == "rock"):
            await ctx.channel.send("player won")
        elif(computerAnswer == "paper" and answer == "scissor"):
            await ctx.channel.send("player won")
        elif(answer == "rock" and computerAnswer == "paper"):
            await ctx.channel.send("computer won")
        elif(answer == "scissor" and computerAnswer == "rock"):
            await ctx.channel.send("computer won")
        elif(answer == "paper" and computerAnswer == "scissor"):
            await ctx.channel.send("computer won")
        else:
            await ctx.channel.send("thats not an input?")
        return

    @rps.error
    async def rps_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return

def setup(client):
    client.add_cog(Rps(client))
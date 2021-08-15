import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import random

class giveMoney(commands.Cog):

    def __init__(self,client,economydb):
        self.client = client
        self.economy = economydb
    
    @commands.command()
    async def beg(self, ctx:Context):
        try:
            random_amount = random.randint(0,1000)
            if random_amount < 800:
                await ctx.channel.send("<:no:860423041335164978>")
                return
            else:
                acc = await self.economy.find_one({'_id': str(ctx.author.id)})
                accBal = int(acc["amount"])
                accBalNew = accBal + random_amount
                await self.economy.replace_one({'_id': str(ctx.author.id)}, {'_id': str(ctx.author.id),'amount': str(accBalNew)}, True)
                await ctx.channel.send(f"take {random_amount} <:rescoin:860198929886478376> you poor poor thing")

        except Exception as error:
            await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(giveMoney(client,client.ecoCol))
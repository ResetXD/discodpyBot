import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import random

class giveMoney(commands.Cog):

    def __init__(self,client,economydb):
        self.client = client
        self.economy = economydb
    
    @commands.command()
    async def bet(self, ctx:Context,howmuch=None):
        if howmuch == None:
            await ctx.channel.send("i dont bet with poor people")
            return
        try:
            random_amount = random.randint(0,1000)
            if random_amount > 400:
                if howmuch == "all" or howmuch == "max":
                    acc = await self.economy.find_one({'_id': str(ctx.author.id)})
                    accBal = int(acc["amount"])
                    accBalNew = 0
                    await self.economy.replace_one({'_id': str(ctx.author.id)}, {'_id': str(ctx.author.id),'amount': str(accBalNew)}, True)
                    await ctx.channel.send(f"haha u lost all your <:rescoin:860198929886478376>")
                    return
                acc = await self.economy.find_one({'_id': str(ctx.author.id)})
                accBal = int(acc["amount"])
                if int(howmuch) > accBal:
                    await ctx.channel.send("yeah sureeee throw more money than u have sureeeeee")
                    return
                else:
                    accBalNew = accBal - int(howmuch)
                    await self.economy.replace_one({'_id': str(ctx.author.id)}, {'_id': str(ctx.author.id),'amount': str(accBalNew)}, True)
                    await ctx.channel.send("u lost haha")
                    return
            else:
                if howmuch == "all" or howmuch == "max":
                    acc = await self.economy.find_one({'_id': str(ctx.author.id)})
                    accBal = int(acc["amount"])
                    accBalNew = accBal*2
                    await self.economy.replace_one({'_id': str(ctx.author.id)}, {'_id': str(ctx.author.id),'amount': str(accBalNew)}, True)
                    await ctx.channel.send("aight u defeated me take my moni {} <:rescoin:860198929886478376>".format(str(accBal)))
                    return
                acc = await self.economy.find_one({'_id': str(ctx.author.id)})
                accBal = int(acc["amount"])
                accBalNew = accBal + int(howmuch)
                await self.economy.replace_one({'_id': str(ctx.author.id)}, {'_id': str(ctx.author.id),'amount': str(accBalNew)}, True)
                await ctx.channel.send(f"aight u defeated me take my moni {howmuch} <:rescoin:860198929886478376>")

        except Exception as error:
            await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(giveMoney(client,client.ecoCol))
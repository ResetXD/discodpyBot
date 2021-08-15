import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from discord.ext.commands.cooldowns import BucketType

class giveMoney(commands.Cog):

    def __init__(self,client,economydb):
        self.client = client
        self.economy = economydb
    
    @commands.command() 
    @commands.cooldown(rate=1,per=86400,type=BucketType.user)
    async def daily(self, ctx:Context):
        try:
            acc = await self.economy.find_one({'_id': str(ctx.author.id)})
            accBal = int(acc["amount"])
            accBalNew = accBal + 15000
            await self.economy.replace_one({'_id': str(ctx.author.id)}, {'_id': str(ctx.author.id),'amount': str(accBalNew)}, True)
            await ctx.channel.send("heres your daily 15,000<:rescoin:860198929886478376>")
        except Exception as e:
            await ctx.channel.send(e)
        return

    @daily.error
    async def daily_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
    
    @commands.command() 
    @commands.cooldown(rate=1,per=604800,type=BucketType.user)
    async def weekly(self, ctx:Context):
        try:
            acc = await self.economy.find_one({'_id': str(ctx.author.id)})
            accBal = int(acc["amount"])
            accBalNew = accBal + 150000
            await self.economy.replace_one({'_id': str(ctx.author.id)}, {'_id': str(ctx.author.id),'amount': str(accBalNew)}, True)
            await ctx.channel.send("heres your daily 150,000<:rescoin:860198929886478376>")
        except Exception as e:
            await ctx.channel.send(e)
        return

    @weekly.error
    async def weekly_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
    
    @commands.command() 
    @commands.cooldown(rate=1,per=2419200,type=BucketType.user)
    async def monthly(self, ctx:Context):
        try:
            acc = await self.economy.find_one({'_id': str(ctx.author.id)})
            accBal = int(acc["amount"])
            accBalNew = accBal + 1500000
            await self.economy.replace_one({'_id': str(ctx.author.id)}, {'_id': str(ctx.author.id),'amount': str(accBalNew)}, True)
            await ctx.channel.send("heres your daily 1,500,000<:rescoin:860198929886478376>")
        except Exception as e:
            await ctx.channel.send(e)
        return

    @monthly.error
    async def monthly_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        
    
def setup(client):
    client.add_cog(giveMoney(client,client.ecoCol))
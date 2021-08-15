import discord
from discord import player
from discord.ext import commands
from discord.ext.commands.context import Context

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def sell(self, ctx:Context,sellable = None,amount=1):
        if sellable == None:
            return await ctx.channel.send("item isnt sellable")
        try:
            playerINFO = await self.client.general.find_one({"_id":str(ctx.author.id)})
        except:
            return await ctx.send("player havent registered")
        cursor = self.client.shop.find()
        a = await cursor.to_list(length=100)
        if playerINFO["guildname"] == "none":
            return await ctx.channel.send("player must be in a guild to sell items")
        for x in a:
            if x["_id"] == sellable:
                acc = playerINFO["inv"]
                acc = acc.split(",")
                acc.pop()
                if int(acc.count(sellable)) >= int(amount):
                    for y in range(int(amount)):
                            acc.remove(sellable)
                    newacc = ""
                    for xy in acc:
                        newacc += xy + ","
                    await ctx.channel.send(newacc)
                    newmoney = int(playerINFO["money"]) + (int(x["value"])*int(amount))
                    newINV = int(playerINFO["items"]) - int(amount) 
                    newinventoryyyy = newacc
                    left = int(x["left"]) + int(amount)
                    await self.client.general.update_one({'_id': str(ctx.author.id)}, {'$set': {'money': str(newmoney),"items":str(newINV),"inv":newinventoryyyy}})
                    await self.client.shop.update_one({'_id': str(sellable)}, {'$set': {"left":left}})
                    return await ctx.channel.send("thank you for selling")
                else:
                    return await ctx.channel.send("amount specified is more than what player have")
                
        return await ctx.channel.send("cant find {0} as sellable".format(sellable))
    
    # @sell.error
    # async def define_error(self, ctx:Context ,error):
    #     await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
    #     return
    
def setup(client):
    client.add_cog(Ping(client))
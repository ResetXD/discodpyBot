import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Ping(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    @commands.is_owner()
    async def addshop(self, ctx:Context,name,value,how_much,image,effect):
        await self.client.shop.insert_one({"_id":name,"value":value,"left":how_much,"image":image,"effect":effect})
        await ctx.channel.send("added the item to the shop")
        return
    
    @addshop.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
    #####################################################################################################

    @commands.command()
    async def shop(self, ctx:Context,what=None):
        if what == None:
            cursor = self.client.shop.find()
            a = await cursor.to_list(length=100)
            embedVar = discord.Embed(title="shop",color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url=ctx.author.avatar_url)
            for x in a:
                embedVar.add_field(name="{0} {1}".format(x["image"],x["_id"]),value="price-{0}\nitem left-{1}".format(x["value"],x["left"]))
            await ctx.channel.send(embed=embedVar)
            return
        else:
            try:
                x = await self.client.shop.find_one({"_id":what})
                embedVar = discord.Embed(title="shop",color = discord.Colour.dark_theme())
                embedVar.set_thumbnail(url=ctx.author.avatar_url)
                embedVar.add_field(name="{0} {1}".format(x["image"],x["_id"]),value="price-{0}\nitem left-{1}\neffects {2}".format(x["value"],x["left"],x["effect"]))
                await ctx.channel.send(embed=embedVar)
                return
            except Exception as e:
                return await ctx.channel.send(f"{e} doesnt exist in this shop")

    
    @shop.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return

    #####################################################################################################

    @commands.command()
    @commands.is_owner()
    async def removeshop(self, ctx:Context,name):
        await self.client.shop.delete_many({'_id': name})
        await ctx.channel.send("removed the item from the shop")
        return
    
    @addshop.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return

    ########################################################################################################

    @commands.command()
    async def buy(self, ctx:Context,itemName,amount=1):
        cursor = self.client.shop.find()
        try:
            playerINFO = await self.client.general.find_one({"_id":str(ctx.author.id)})
        except:
            return await ctx.send("player havent registered")
        a = await cursor.to_list(length=100)
        for x in a:
            leftt = int(x["left"])
            if itemName == x["_id"]:
                if int(x["left"]) <= 0:
                    return await ctx.send("item is finished")
                if int(x["value"])*int(amount) > int(playerINFO["money"]):
                    return await ctx.send("player doesnt have much money")
                else:
                    newmoney = int(playerINFO["money"]) - int(x["value"])*int(amount)
                    newINV = int(playerINFO["items"]) + int(amount)
                    newinventoryyyy = playerINFO["inv"] 
                    for z in range(int(amount)):
                        if leftt <= 0:
                            await ctx.send("item is finished")
                            newLeft = int(x["left"]) - int(amount)
                            newINV = int(playerINFO["items"]) + int(x["left"])
                            newmoney = int(playerINFO["money"]) - int(x["value"])*int(x["left"])
                            await self.client.general.update_one({'_id': str(ctx.author.id)}, {'$set': {'money': str(newmoney),"items":str(newINV),"inv":newinventoryyyy}})
                            await self.client.shop.update_one({'_id': str(itemName)}, {'$set': {"left":"0"}})
                            return
                        newinventoryyyy +=  x["_id"] + ","               
                        leftt -= 1     
                    newLeft = int(x["left"]) - int(amount)
                    await self.client.general.update_one({'_id': str(ctx.author.id)}, {'$set': {'money': str(newmoney),"items":str(newINV),"inv":newinventoryyyy}})
                    await self.client.shop.update_one({'_id': str(itemName)}, {'$set': {"left":str(newLeft)}})
                    return await ctx.channel.send("thank your for your purchase")
        await ctx.channel.send("cant find this item on the shop")
        return
    
    @buy.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return

    ##################################################################################################

    @commands.command(aliases = ["proposeshop"])
    async def tryshop(self, ctx:Context,name,value,image,*,items_to_make_this_item):
        chan = self.client.get_channel(872150058072694854)
        embedVar = discord.Embed(title = "new shop item" , color = discord.Colour.dark_theme())
        embedVar.set_thumbnail(url = ctx.author.avatar_url)
        embedVar.add_field(name = "name",value = f"{name}",inline = False)
        embedVar.add_field(name = "value",value = f"{value}",inline = False)
        embedVar.add_field(name = "image",value = f"{image}",inline = False)
        embedVar.add_field(name = "item to make this item",value = f"{items_to_make_this_item}",inline = False)
        await chan.send(embed = embedVar)
        await ctx.channel.send("your item is up for review sucessfully")
        return
    
    @addshop.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return

def setup(client):
    client.add_cog(Ping(client))
import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class account(commands.Cog):

    def __init__(self,client,economydb):
        self.client = client
        self.guilddb = economydb
    
    @commands.command(aliases = ["guildinfo"])
    async def guild(self, ctx:Context,guildID = None):
        if guildID == None:
            generalINFO = await self.client.general.find_one({'_id': str(ctx.author.id)})
            guildID = generalINFO["guildname"]
            if guildID == "none":
                return await ctx.channel.send("player isnt in a guild yet")
        try:
            acc = await self.guilddb.find_one({'_id': str(guildID)})
            embedVar = discord.Embed(title = "guild info" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = acc["image"])
            embedVar.add_field(name = "name" , value = "{0}".format(acc["_id"]),inline = True)
            embedVar.add_field(name = "level" , value = "{0}".format(acc["level"]),inline = True)
            embedVar.add_field(name = "owner" , value = "<@{0}>".format(acc["owner"]),inline = True)
            embedVar.add_field(name = "no of members" , value = "{0}".format(acc["members"]),inline = True)
            return await ctx.channel.send(embed = embedVar)
        except Exception as e:
            return await ctx.channel.send(e)
    
    ##################################################################################################
    
    @commands.command()
    async def createguild(self, ctx:Context):
        def check1(m):
            m = m.content
            return m.lower() in ["yes","y"]
        def check2(m):
            return "cg " in str(m.content) or "cg " in str(m.content) 

        try:
            generalINFO = await self.client.general.find_one({'_id': str(ctx.author.id)})
            if not generalINFO["guildname"] == "none":
                return await ctx.channel.send("you are already in a guild ,leave the guild to try again")
            await ctx.channel.send("creating a guild requires 1,00,000 coins are you sure? (yes/y/n/no)")
            msg = await self.client.wait_for('message', check=check1)
            if int(generalINFO["money"]) < 100000:
                return await ctx.channel.send("you dont have enough money to make a guild")
            await ctx.channel.send("(start the name and url with \"cg \" it will be removed in the real name and url)")
            await ctx.channel.send("name of the guild?")
            msg = await self.client.wait_for('message', check=check2)   
            guildNAME = str(msg.content)
            await ctx.channel.send("guild logo?(http/https link to an image)")
            msg = await self.client.wait_for('message', check=check2)   
            guildIMAGE = str(msg.content)
            moneyleft = int(generalINFO["money"]) - 100000
            await self.guilddb.insert_one({"_id":guildNAME[3:],"image":guildIMAGE[3:],"members":"1","level":"1","owner":str(ctx.author.id)})
            await self.client.general.update_one({'_id': str(ctx.author.id)}, {'$set': {'guildname': str(guildNAME[3:]),"money":str(moneyleft)}})
            await ctx.channel.send("congrats on forming a guild bring more people and become the best")
        except Exception as e:
            return await ctx.channel.send(e)
    
    ##################################################################################################
    
    @commands.command(aliases = ["guildjoin"])
    async def joinguild(self, ctx:Context,*,guildID = None):
        def check1(m):
            m = m.content
            return m.lower() in ["yes","y"]
        if guildID == None:
            return await ctx.channel.send("please provide the guild name")
        generalINFO = await self.client.general.find_one({'_id': str(ctx.author.id)})
        if not generalINFO["guildname"] == "none":
            return await ctx.channel.send("player is already are in a guild or havent registered")
        await ctx.channel.send("you are about to join {0} are your sure?(yes/y/n/no)".format(guildID))
        msg = await self.client.wait_for('message', check=check1)
        try:
            try:
                guildinfo = await self.guilddb.find_one({'_id': str(guildID)})
                guildname = guildinfo["_id"]
            except:
                return await ctx.channel.send("guild doesnt exist")
            totalmembers = int(guildinfo["members"]) + 1
            money = int(generalINFO["money"]) + 1000
            await self.client.general.update_one({'_id': str(ctx.author.id)}, {'$set': {'guildname': str(guildname),"money":int(money)}})
            await self.guilddb.update_one({'_id': str(guildID)}, {'$set': {"members":str(totalmembers)} } )
            
            await ctx.channel.send("congrats on joining {0}. your are given 1000 money for starting".format(guildinfo["_id"]))
        except Exception as e:  
            return await ctx.channel.send(e)
    
    ##################################################################################################

    @commands.command(aliases = ["guildleave"])
    async def leaveguild(self, ctx:Context):
        def check1(m):
            m = m.content
            return m.lower() in ["yes","y"]
        generalINFO = await self.client.general.find_one({'_id': str(ctx.author.id)})
        if generalINFO["guildname"] == "none":
            return await ctx.channel.send("player is isnt in a guild yet")
        await ctx.channel.send("you are about to leave {0} are your sure?(yes/y/n/no)".format(generalINFO["guildname"]))
        msg = await self.client.wait_for('message', check=check1,timeout = 10)
        try:
            try:
                guildinfo = await self.guilddb.find_one({'_id': str(generalINFO["guildname"])})
                guildname = guildinfo["_id"]
                if str(guildinfo["owner"]) == str(generalINFO["_id"]):
                    return await ctx.channel.send("owner cant leave his own guild unless he disbandon it")
            except:
                return await ctx.channel.send("guild doesnt exist")
            totalmembers = int(guildinfo["members"]) - 1
            await self.client.general.update_one({'_id': str(ctx.author.id)}, {'$set': {'guildname': "none"}})
            await self.client.general.update_one({'_id': str(guildname)}, {'$set': {"members":str(totalmembers)} } )

            await ctx.channel.send("you left {0}".format(guildinfo["_id"]))
        except Exception as e:
            return await ctx.channel.send(e)
        
    ##################################################################################################

    @commands.command(aliases = ["gm"])
    async def guildmember(self, ctx:Context):
        generalINFO = await self.client.general.find_one({'_id': str(ctx.author.id)})
        guildID = generalINFO["guildname"]
        guildinfo = await self.guilddb.find_one({'_id': str(generalINFO["guildname"])})
        if guildID == "none":
            return await ctx.channel.send("player not in guild")
        if not guildinfo["owner"] == str(ctx.author.id):
            return await ctx.channel.send("player isnt allowed to access this information")
        try:
            memberinfo = self.client.general.find({'guildname': guildinfo["_id"]})
            await ctx.channel.send("ok 4")
            des = ""
            for x in await memberinfo.to_list(length=10000):
                des += "<@" + x["_id"] + ">\n"
            embedVar = discord.Embed(title="members list",description = des,color = discord.Colour.dark_theme())
            return await ctx.channel.send(embed = embedVar)
        except Exception as e:
            return await ctx.channel.send(e)

def setup(client):
    client.add_cog(account(client,client.guild))
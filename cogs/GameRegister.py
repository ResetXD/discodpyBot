import random
import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class account(commands.Cog):

    def __init__(self,client,economydb):
        self.client = client
        self.registerdb = economydb
    
    @commands.command(aliases = ["reg"])
    async def register(self, ctx:Context):
        def responseChecker(m):
            m = m.content
            return m.lower() in ["yes","y"]
        lll = ["thief","archer","assassin","ranger","priest","dark priest","wizard","magic item craftsman","adventurer"]
        classtype = random.choice(lll)
        if classtype == None:
            return await ctx.invoke(self.client.get_command('help') ,"register")
        try:
            acc = await self.registerdb.find_one({'_id': str(ctx.author.id)})
            return await ctx.channel.send("player have already registered with class {0}".format(acc["class"]))
        except:
            if classtype == "archer" or classtype == "Archer":
                await ctx.channel.send(f"welcome player to this game you are getting registered as {classtype} are you sure?(yes/y/n/no)")
                msg = await self.client.wait_for('message', check=responseChecker)
                await ctx.channel.send('welcome {0}! join a guild(gives starters stuff ahem),make a party and start your adventure as an {1}'.format(msg.author.mention,classtype))
                a = await self.registerdb.insert_one({'_id': str(ctx.author.id),'class':str(classtype),"money":"0","guildname":"none","items":"0","party":"none","chp":"100","cmana":"100","level":"1","inv":"","exp":"0","hp":"100","mana":"100"})
                return
            elif classtype == "thief" or classtype == "Thief":
                await ctx.channel.send(f"welcome player to this game you are getting registered as {classtype} are you sure?(yes/y/n/no)")
                msg = await self.client.wait_for('message', check=responseChecker)
                await ctx.channel.send('welcome {0}! join a guild(gives starters stuff ahem),make a party and start your adventure as an {1}'.format(msg.author.mention,classtype))
                a = await self.registerdb.insert_one({'_id': str(ctx.author.id),'class':str(classtype),"money":"0","guildname":"none","items":"0","party":"none","chp":"100","cmana":"100","level":"1","inv":"","exp":"0","hp":"100","mana":"100"})
                return
            elif classtype == "assassin" or classtype == "Assassin":
                await ctx.channel.send(f"welcome player to this game you are getting registered as {classtype} are you sure?(yes/y/n/no)")
                msg = await self.client.wait_for('message', check=responseChecker)
                await ctx.channel.send('welcome {0}! join a guild(gives starters stuff ahem),make a party and start your adventure as an {1}'.format(msg.author.mention,classtype))
                a = await self.registerdb.insert_one({'_id': str(ctx.author.id),'class':str(classtype),"money":"0","guildname":"none","items":"0","party":"none","chp":"100","cmana":"100","level":"1","inv":"","exp":"0","hp":"100","mana":"100"})
                return
            elif classtype == "ranger" or classtype == "Ranger":
                await ctx.channel.send(f"welcome player to this game you are getting registered as {classtype} are you sure?(yes/y/n/no)")
                msg = await self.client.wait_for('message', check=responseChecker)
                await ctx.channel.send('welcome {0}! join a guild(gives starters stuff ahem),make a party and start your adventure as an {1}'.format(msg.author.mention,classtype))
                a = await self.registerdb.insert_one({'_id': str(ctx.author.id),'class':str(classtype),"money":"0","guildname":"none","items":"0","party":"none","chp":"100","cmana":"100","level":"1","inv":"","exp":"0","hp":"100","mana":"100"})
                return
            elif classtype == "priest" or classtype == "Priest":
                await ctx.channel.send(f"welcome player to this game you are getting registered as {classtype} are you sure?(yes/y/n/no)")
                msg = await self.client.wait_for('message', check=responseChecker)
                await ctx.channel.send('welcome {0}! join a guild(gives starters stuff ahem),make a party and start your adventure as an {1}'.format(msg.author.mention,classtype))
                a = await self.registerdb.insert_one({'_id': str(ctx.author.id),'class':str(classtype),"money":"0","guildname":"none","items":"0","party":"none","chp":"150","cmana":"200","level":"1","inv":"","exp":"0","hp":"150","mana":"200"})
                return
            elif classtype == "dark priest" or classtype == "Dark priest":
                await ctx.channel.send(f"welcome player to this game you are getting registered as {classtype} are you sure?(yes/y/n/no)")
                msg = await self.client.wait_for('message', check=responseChecker)
                await ctx.channel.send('welcome {0}! join a guild(gives starters stuff ahem),make a party and start your adventure as an {1}'.format(msg.author.mention,classtype))
                a = await self.registerdb.insert_one({'_id': str(ctx.author.id),'class':str(classtype),"money":"0","guildname":"none","items":"0","party":"none","chp":"150","cmana":"200","level":"1","inv":"","exp":"0","hp":"150","mana":"200"})
                return
            elif classtype == "wizard" or classtype == "Wizard":
                await ctx.channel.send(f"welcome player to this game you are getting registered as {classtype} are you sure?(yes/y/n/no)")
                msg = await self.client.wait_for('message', check=responseChecker)
                await ctx.channel.send('welcome {0}! join a guild(gives starters stuff ahem),make a party and start your adventure as an {1}'.format(msg.author.mention,classtype))
                a = await self.registerdb.insert_one({'_id': str(ctx.author.id),'class':str(classtype),"money":"0","guildname":"none","items":"0","party":"none","chp":"150","cmana":"300","level":"1","inv":"","exp":"0","hp":"150","mana":"300"})
                return
            elif classtype == "magic item craftsman" or classtype == "Magic item craftsman":
                await ctx.channel.send(f"welcome player to this game you are getting registered as {classtype} are you sure?(yes/y/n/no)")
                msg = await self.client.wait_for('message', check=responseChecker)
                await ctx.channel.send('welcome {0}! join a guild(gives starters stuff ahem),make a party and start your adventure as an {1}'.format(msg.author.mention,classtype))
                a = await self.registerdb.insert_one({'_id': str(ctx.author.id),'class':str(classtype),"money":"0","guildname":"none","items":"0","party":"none","chp":"100","cmana":"300","level":"1","inv":"","exp":"0","hp":"100","mana":"300"})
                return
            elif classtype == "adventurer" or classtype == "Adventurer":
                await ctx.channel.send(f"welcome player to this game you are getting registered as {classtype} are you sure?(yes/y/n/no)")
                msg = await self.client.wait_for('message', check=responseChecker)
                await ctx.channel.send('welcome {0}! join a guild(gives starters stuff ahem),make a party and start your adventure as an {1}'.format(msg.author.mention,classtype))
                a = await self.registerdb.insert_one({'_id': str(ctx.author.id),'class':str(classtype),"money":"0","guildname":"none","items":"0","party":"none","chp":"100","cmana":"50","level":"1","inv":"","exp":"0","hp":"100","mana":"50"})
                return
            else:
                return await ctx.channel.send(f"{classtype} isnt a valid class")
            
    
def setup(client):
    client.add_cog(account(client,client.general))
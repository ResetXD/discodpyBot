import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class account(commands.Cog):

    def __init__(self,client,economydb):
        self.client = client
        self.registerdb = economydb
    
    @commands.command(aliases = ["playerinfo"])
    async def info(self, ctx:Context,who:discord.Member = None):
        if who == None:
            who = ctx.author
        try:
            acc = await self.registerdb.find_one({'_id': str(who.id)})
            embedVar = discord.Embed(title = "player info" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = who.avatar_url)
            embedVar.add_field(name = "name" , value = "{0}".format(who.display_name),inline = True)
            embedVar.add_field(name = "class" , value = "{0}".format(acc["class"]),inline = True)
            embedVar.add_field(name = "total HP" , value = "{0}".format(acc["hp"]),inline = True)
            embedVar.add_field(name = "total mana" , value = "{0}".format(acc["mana"]),inline = True)
            embedVar.add_field(name = "left HP" , value = "{0}".format(acc["chp"]),inline = True)
            embedVar.add_field(name = "left mana" , value = "{0}".format(acc["cmana"]),inline = True)
            embedVar.add_field(name = "guild" , value = "{0}".format(acc["guildname"]),inline = True)
            embedVar.add_field(name = "party" , value = "{0}".format(acc["party"]),inline = True)
            embedVar.add_field(name = "level" , value = "{0}".format(acc["level"]),inline = True)
            embedVar.add_field(name = "exp" , value = "{0}".format(acc["exp"]),inline = True)
            embedVar.add_field(name = "money" , value = "{0}".format(acc["money"]),inline = True)
            embedVar.add_field(name = "item owns" , value = "{0}".format(acc["items"]),inline = True)
            return await ctx.channel.send(embed = embedVar)
        except Exception as e:
            return await ctx.channel.send("player isnt registered yet")
    
    ########################################################################################

    @commands.command(aliases = ["inventory"])
    async def inv(self, ctx:Context,who:discord.Member = None):
        if who == None:
            who = ctx.author
        try:
            acc = await self.registerdb.find_one({'_id': str(who.id)})
            acc = acc["inv"]
            acc = acc.split(",")
            acc.pop()
            aa = ""
            for x in acc:
                if acc.count(x) != 0:
                    aa += x +" X " + str(acc.count(x)) +"\n"
                try:
                    acc = list(filter(lambda a: a != x, acc))
                except Exception as e:
                    aa += str(e)
                    
            embedVar = discord.Embed(title = "player inventory" , color = discord.Colour.dark_theme(),description=aa)
            embedVar.set_thumbnail(url = who.avatar_url)
            return await ctx.channel.send(embed = embedVar)
        except Exception as e:
            return await ctx.channel.send(f"player isnt registered yet or {e}")

            
    
def setup(client):
    client.add_cog(account(client,client.general))
import discord
from discord.ext import commands
from discord.ext.commands.context import Context
import json

class Ping(commands.Cog):

    def __init__(self,client,db):
        self.client = client
        self.afk = db
    
    @commands.command(aliases = ["prefix"])
    @commands.has_permissions(administrator = True)
    async def setprefix(self, ctx:Context,*,why):
        prefix_json = open("prefix.json", "r")
        js = json.load(prefix_json)
        prefix_json.close()
        js[f"{ctx.guild.id}"] = why
        a_file = open("prefix.json", "w")
        json.dump(js, a_file)
        a_file.close()
        await ctx.channel.send(f"new prefix for this server {why}")
        return
    
    @setprefix.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(Ping(client,client.afk))
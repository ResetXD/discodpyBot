import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Ping(commands.Cog):

    def __init__(self,client,coll):
        self.client = client
        self.col = coll
    
    @commands.command(aliases = ["suc"])
    async def suggestionchannel(self,ctx:Context,channelID:discord.TextChannel):
        if ctx.message.author.guild_permissions.administrator:
            try:
                await self.col.insert_one({"_id" : ctx.guild.id, "channelID": channelID.id})
                await ctx.channel.send("added your guild in the database")
                return
            except:
                myquery = { "_id": ctx.guild.id }
                newvalues = { "$set": { "channelID": channelID.id} }
                await self.col.update_one(myquery, newvalues)
                await ctx.channel.send("changed to the new channel :D")
                return
        else:
            await ctx.channel.send("this is an adminstrator only command")
    
    @suggestionchannel.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return

    @commands.command()
    async def suggest(self,ctx:Context,*,message=None):
        a = await self.col.find_one({"_id": ctx.guild.id})
        channel = self.client.get_channel(int(a["channelID"]))
        embed = discord.Embed(title="suggestions",color = discord.Colour.gold())
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="Sender", value = f"{ctx.author.mention}", inline=False)
        embed.add_field(name="suggestion", value = message, inline=False)
        a = await channel.send(embed = embed)
        await a.add_reaction("⬆️")
        await a.add_reaction("⬇️")
        return
def setup(client):
    client.add_cog(Ping(client,client.suggest))
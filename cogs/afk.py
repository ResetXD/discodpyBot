import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Ping(commands.Cog):

    def __init__(self,client,db):
        self.client = client
        self.afk = db
    
    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            afkID = message.mentions[0]
            info = await self.afk.find_one({'_id': str(afkID.id)})
            reason = info["reason"]
            await message.channel.send(f"{afkID} is afk for {reason}")
        except:
            info1 = await self.afk.find_one({'_id': str(message.author.id)})
            try:
                if str(message.author.id) == str(info1["_id"]):
                    await message.channel.send(f"removed u from afk {message.author}")
                    await self.afk.delete_many({'_id': str(message.author.id)})
            except:
                pass

    
    @commands.command()
    async def afk(self, ctx:Context,*,why="afk"):
        await self.afk.replace_one({'_id': str(ctx.author.id)}, {'_id': str(ctx.author.id),'reason':str(why)}, True)
        await ctx.channel.send(f"ok you afk for \"{why}\" now")
        return
    
    @afk.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(Ping(client,client.afk))
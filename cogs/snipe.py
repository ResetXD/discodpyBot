import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Warn(commands.Cog):

    def __init__(self,client,collection):
        self.client = client
        self.coll = collection
    
    @commands.command()
    async def snipe(self, ctx:Context):
        try:
            case = await self.coll.find_one({'_id': str(ctx.channel.id)})
            msg = case["message"]
            auth = case["author"]
            embedVar = discord.Embed(title = "sniped this message" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "author" , value = f"{auth}",inline = False)
            embedVar.add_field(name = "message" , value = f"{msg}",inline = False)
            await ctx.channel.send(embed = embedVar)
            return

        except:
            await ctx.channel.send("nothing to snipe here Dang!")
    @snipe.error
    async def nickname_error(self, ctx:Context ,error):
        return await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))

def setup(client):
    client.add_cog(Warn(client,client.snipe))
import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Ping(commands.Cog):

    def __init__(self,client,coll):
        self.client = client
        self.col = coll
    
    @commands.command(aliases = ["setchannel"])
    async def sc(self,ctx:Context,channelID:discord.TextChannel):
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.channel.send("this command only work in a guild channel")
            return
        else:
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
        
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def reply(self,ctx:Context,user_id:discord.Member,*,message):
        user = await self.client.fetch_user(user_id.id)
        mmembed=discord.Embed(title="Message recieved", color=discord.Color.gold())
        mmembed.add_field(name=f"{ctx.author}", value=f"{message}", inline=False)
        mmembed.set_footer(text=f"from guild {ctx.guild}")
        mmembed.set_thumbnail(url=f"{ctx.author.avatar_url}")
        await discord.channel.DMChannel.send(user, embed=mmembed)

    @commands.command()
    async def mail(self,ctx:Context,guildID:int,*,message=None):
        if isinstance(ctx.channel, discord.channel.DMChannel):
            a = await self.col.find_one({"_id": guildID })
            channel = self.client.get_channel(int(a["channelID"]))
            embed = discord.Embed(title="MOD MAIL",color = discord.Colour.gold())
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.add_field(name="Sender", value = f"{ctx.author.mention}", inline=False)
            embed.add_field(name="message", value = message, inline=False)
            embed.set_footer(text=f"Sender ID - {ctx.author.id}")
            await channel.send(embed = embed)
            return
        else:
            return
        
def setup(client):
    client.add_cog(Ping(client,client.col))
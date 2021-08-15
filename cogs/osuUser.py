import asyncio
import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from osu import user
from osu import init

class osuUser(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['osu'])
    async def osuuser(self, ctx:Context,name = None):
        if name == None:
            try:
                playerinfo = await self.client.osu.find_one({'_id': str(ctx.author.id)})
                name = playerinfo["username"]
            except:
                await ctx.channel.send("no user provided")
                return
        token = init.Init(key="osu token")
        userinfo = user.User(token=token)
        userJson = await userinfo.get_user(username=name)
        link = "https://osu.ppy.sh/users/" + userJson["user_id"]
        co = ":flag_"+userJson["country"]+":"
        embed = discord.Embed(title = f"osu! user: {name}!" , color = discord.Colour.dark_theme())
        embed.add_field(name="username",value=userJson["username"],inline=True)
        embed.add_field(name=f"coutry rank{co.lower()}",value=userJson["pp_country_rank"],inline=True)
        embed.add_field(name="level📈",value=userJson["level"],inline=True)
        embed.add_field(name="playcount",value=userJson["playcount"],inline=True)
        embed.add_field(name="ranked score",value=userJson["ranked_score"],inline=True)
        embed.add_field(name="accuracy",value=userJson["accuracy"],inline=True)
        embed.add_field(name="PP😔",value=userJson["pp_raw"],inline=True)     
        embed.add_field(name="count rank <:ss:853965559058006037>",value=userJson["count_rank_ssh"],inline=True)
        embed.add_field(name="count rank <:ssh:853965558629531660>",value=userJson["count_rank_ss"],inline=True)
        embed.add_field(name="count rank <:sh:853965558427680770>",value=userJson["count_rank_sh"],inline=True)
        embed.add_field(name="count rank <:s_:853965558638968892>",value=userJson["count_rank_s"],inline=True)
        embed.add_field(name="count rank <:a_:853965558810411018>",value=userJson["count_rank_a"],inline=True)
        embed.add_field(name="link",value=f"<:osu:853962496951975977>[osupfp]({link})",inline=True)
        embed.set_thumbnail(url=userinfo.get_user_pfp_url(user_id=userJson["user_id"]))
        await ctx.channel.send(embed = embed)
        return
    
    @commands.command()
    async def setosu(self, ctx:Context,name):
        await self.client.osu.replace_one({'_id': str(ctx.author.id)}, {'_id': str(ctx.author.id),'username':str(name)}, True)
        return await ctx.channel.send("added you to the database use this command again if you got your osu username wrong")
def setup(client):
    client.add_cog(osuUser(client))
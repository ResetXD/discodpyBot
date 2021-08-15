import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from osu import user
from osu import init
from osu import beatmap

class osuUser(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['recentplay','recent',"r"])
    async def osurecent(self, ctx:Context,name = None):
        if name == None:
            try:
                playerinfo = await self.client.osu.find_one({'_id': str(ctx.author.id)})
                name = playerinfo["username"]
            except:
                await ctx.channel.send("no user provided")
                return
    
        token = init.Init(key="osu token")
        userinfo = user.User(token=token)
        beatmaptemp = beatmap.Beatmap(token=token)
        recentJson = await userinfo.get_user_recent(username=name)
        if recentJson == 0:
            await ctx.channel.send("no recent plays")
            return
        else:
            beatmapJson = await beatmaptemp.get_beatmap(beatmapID=recentJson["beatmap_id"])
            beatmapurl = "https://osu.ppy.sh/beatmapsets/"+ beatmapJson["beatmapset_id"]
            btname = beatmapJson["title"]
            bt_score = recentJson["count300"]+"•"+recentJson["count100"]+"•"+recentJson["count50"]+"•"+recentJson["countmiss"]
            embed = discord.Embed(title=f"{name} 's recent play", color = discord.Colour.dark_theme())
            embed.add_field(name=f"title",value= f"[{btname}]({beatmapurl})",inline=True)
            embed.add_field(name="score-{}".format(recentJson["rank"]),value="{0} with {1}".format(recentJson["score"],bt_score),inline=True)
            embed.add_field(name="maxcombo",value= "{}".format(recentJson["maxcombo"]),inline=False)
            embed.add_field(name="difficulty",value="{}".format(beatmapJson["version"]),inline=True)
            embed.set_thumbnail(url= beatmaptemp.get_beatmap_thumbnail_url(beatmapset_id=beatmapJson["beatmapset_id"]))
            await ctx.channel.send(embed=embed)
            return
    
def setup(client):
    client.add_cog(osuUser(client))
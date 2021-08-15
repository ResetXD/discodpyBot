import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from osu import user
from osu import init
from osu import beatmap

class osuTop(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['top','topplay','osutop'])
    async def t(self, ctx:Context,name = None):
        if name == None:
            await ctx.channel.send("no user provided")
            return
        else:
            token = init.Init(key="osu token")
            userinfo = user.User(token=token)
            beatmaptemp = beatmap.Beatmap(token=token)
            recentJson = await userinfo.get_user_recent(username=name)
            if recentJson == 0:
                await ctx.channel.send("no recent plays")
                return
            else:
                beatmapJson = await beatmaptemp.get_beatmap(beatmapID=recentJson["beatmap_id"])
                beatMapName = beatmapJson["title"]
                await ctx.channel.send(beatmapJson["title"])
                embed = discord.Embed(title = f"osu! user: {name} 's recent play" , color = discord.Colour.dark_theme())
                embed.add_field(name=f"[{beatMapName}]()",value="",inline=True)
                embed.set_thumbnail(url=beatmaptemp.get_beatmap_cover_url(beatmapset_id=beatmapJson["beatmapset_id"]))
                
                
                await ctx.channel.send(embed=embed)
                return
    
def setup(client):
    client.add_cog(osuTop(client))
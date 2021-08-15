import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class WhoAmI(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command(aliases = ['whois','ui','aboutme','me'])
    async def whoami(self,ctx : Context, *, user: discord.Member = None): # b'\xfc'
        if user is None:
            user = ctx.author      
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(title = "whoami", color = discord.Colour.dark_theme())
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name = 'general info',value = 'id: ' + str(user.id) + "\nname: " + str(user.mention), inline = True)
        embed.add_field(name="Joined on", value=user.joined_at.strftime(date_format))
        # members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        # embed.add_field(name="Join position", value=str(members.index(user)+1))
        embed.add_field(name="Registered", value=user.created_at.strftime(date_format), inline = True)
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=True)
        embed.add_field(name="top role", value=user.top_role, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        embed.add_field(name="Guild permissions", value=perm_string, inline=False)
        embed.set_footer(text='asked by ' + "{}".format(ctx.author))
        return await ctx.send(embed=embed)

    @whoami.error
    async def yeet_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(WhoAmI(client))
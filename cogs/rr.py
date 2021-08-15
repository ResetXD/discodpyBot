import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Ping(commands.Cog):

    def __init__(self,client,reaction):
        self.client = client
        self.rr = reaction
    
    @commands.command(aliases = ['reactionrole'])
    async def rr(self, ctx:Context,messageID,roleID,emojiID):
        await self.rr.replace_one({'_id': str(messageID)}, {'_id': str(messageID),'roleID':str(roleID),'emojiID':str(emojiID)}, True)
        msg = await discord.TextChannel.fetch_message(ctx.channel,int(messageID))
        emo = await discord.Guild.fetch_emoji(ctx.guild,int(emojiID))
        await msg.add_reaction(emo)
        return
    @rr.error
    async def define_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return
    
def setup(client):
    client.add_cog(Ping(client,client.rr))
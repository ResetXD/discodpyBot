import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Purge(commands.Cog):

    def __init__(self,client,guilddb,messagedb,embeddb):
        self.client = client
        self.starguild = guilddb
        self.starmessage = messagedb
        self.starembed = embeddb

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        # if str(payload.emoji) == "⭐":
        #     try:
        #         messagedb = await self.starmessage.find_one({'_id': str(payload.message_id)})
        #         guilddb = await self.starguild.find_one({'_id': str(payload.guild_id)})
        #         mess = int(messagedb["rr"]) + 1
        #         channel = self.client.get_channel(int(payload.channel_id))
        #         msg = await channel.fetch_message(int(payload.message_id))
        #         await self.starmessage.replace_one({'_id': str(payload.message_id)}, {'_id': str(payload.message_id),"author":str(msg.author),"message":str(msg.content),"rr":str(mess)}, True)
        #         if mess >= int(guilddb["howmuch"]):
        #             channel = self.client.get_channel(int(guilddb["channel"]))
        #             msg = await channel.send("message {0}".format(messagedb["message"]))
        #             print(msg.id)
        #         else:
        #             pass

        #     except:
        #         channel = self.client.get_channel(int(payload.channel_id))
        #         msg = await channel.fetch_message(int(payload.message_id))
        #         await self.starmessage.replace_one({'_id': str(payload.message_id)}, {'_id': str(payload.message_id),"author":str(msg.author),"message":str(msg.content),"rr":str(1)}, True)
        # else:
        #     pass
        pass

    @commands.command()
    async def setstarguild(self,ctx: Context , channel:discord.TextChannel = None,howmuch=2):
        # try:
        #     await self.starguild.replace_one({'_id': str(ctx.guild.id)}, {'_id': str(ctx.guild.id),"howmuch":str(howmuch),"channel":str(channel.id)}, True)
        #     await ctx.channel.send(f"message will be sent to {channel} on {howmuch}⭐")
        #     return
        # except:
        #     pass
        pass

    @setstarguild.error
    async def purge_error(self,ctx:Context ,error):
        await ctx.channel.send(error)
    

def setup(client):
    client.add_cog(Purge(client,client.starguild,client.starmessage,client.starembed))
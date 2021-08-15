import discord
from discord.ext import commands
from discord.ext.commands.context import Context
from popcatapi import  popcatAI

class _8ball(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command(aliases = ['8ball' , '8b',"8BALL","8B"])
    async def _8ball(self,ctx : Context ,*, ques = None):
        a = popcatAI.chatbot()
        b = await a.get_response(message=ques)
        await ctx.channel.send(b)
    
    @_8ball.error
    async def _8ball_error(self, ctx:Context ,error):
        await ctx.channel.send("<:kurumi_ara_ara:865856459383898113> "+str(error))
        return



    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.id == self.client.user.id:
            try:
                a = await self.client.annoy.find_one({"_id":str(message.channel.id)})
                if str(message.channel.id) == a["_id"]:
                    a = popcatAI.chatbot()
                    b = await a.get_response(message=message.content)
                    await message.channel.send(b)
            except:
                pass


    @commands.command()
    async def annoy(self,ctx:Context,what):
        try:
            if what == "on":
                await self.client.annoy.insert_one({"_id":str(ctx.channel.id)})
                await ctx.channel.send("its on")
            elif what == "off":
                await self.client.annoy.delete_one({"_id":str(ctx.channel.id)})
                await ctx.channel.send("its off")
            else:
                await ctx.send("¯\\\_(ツ)\_\/¯")
        except:
            pass
def setup(client):
    client.add_cog(_8ball(client))
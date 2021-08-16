import os
import asyncpraw
import discord
import motor.motor_asyncio
from discord.ext import commands
from discord.ext.commands.context import Context
import json

mongoClient = motor.motor_asyncio.AsyncIOMotorClient("yours NOT MINE monogdb connector")

# from keep_alive import keep_alive

# keep_alive()

reddit = asyncpraw.Reddit(
    client_id= "reddit api client id",
    client_secret= "reddit api client secret",
    user_agent="the other thing that is with those two things",
)

db = mongoClient['discord']
db1 = mongoClient["adventure"]
guildJoinCollection = db['guildJoin']

intents = discord.Intents.default()
intents.members = True

def get_prefix(client, message): 
    with open('prefix.json', 'r') as f:
        prefixes = json.load(f)
    try:
        return prefixes[str(message.guild.id)]
    except:
        return ["c ", "C ","chan ","Chan ","CHAN","CHAN ","chan","Chan","Res ","res ","res","RES","Res"]

client = commands.Bot(command_prefix = (get_prefix),intents=intents)

client.warnCol = db["warn"]
client.ecoCol = db["economy"]
client.bj = db["blackJack"]
client.rr = db["rr"]
client.snipe = db["snipe"]
client.afk = db["afk"]
client.starguild = db["starguild"]
client.starmessage = db["starmessage"]
client.starembed = db["starembed"]
client.wallpaperdb = db["wallpaperdb"]
client.kurumi = db["kurumi"]
client.col = db["modMail"]
client.osu = db["osu"]
client.suggest = db["suggest"]
client.annoy = db["annoy"]

#############################################

client.general = db1["genereal"]
client.guild = db1["guild"]
client.shop = db1["shop"]


@client.event
async def on_ready():
    print(f'connected as {client.user}')
    e = await client.fetch_guilds().flatten()
    servers = client.guilds
    total = 0
    for guild in servers:
        total += int(guild.member_count)
    game = discord.Game(f"managing players in {len(e)} servers with {total} members")
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_guild_join(g):
    success = False
    i = 0
    while not success:
        try:
            await g.channels[i].send("hi users my prefix is \"chan \" if you dont know what i do then use \"chan help\"")
        except (discord.Forbidden, AttributeError):
            i += 1
        except IndexError:
            pass
        else:
            success = True
    servers = client.guilds
    total = 0
    for guild in servers:
        total += int(guild.member_count)
    e = await client.fetch_guilds().flatten()
    game = discord.Game(f"managing players in {len(e)} servers with {total} members")
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.command()
@commands.has_permissions(administrator = True)
async def setwelcome(ctx:Context,channel: discord.TextChannel,*,messageTOShow=None):
    if messageTOShow == None:
        messageTOShow = "joined yay"
    try:
        await guildJoinCollection.replace_one({'_id': str(ctx.guild.id)}, {'_id': str(ctx.guild.id),'channelID':str(channel.id),'message':str(messageTOShow)}, True)
    except:
        pass

@client.event
async def on_member_join(g):
    try:
        channelcol = await guildJoinCollection.find_one({'_id': str(g.guild.id)})
        channel = client.get_channel(int(channelcol["channelID"]))
        one = g.name.replace(' ','%20')
        two = str(channelcol["message"]).replace(' ','%20')
        three = "welcome%20to%20the%20server"
        avatar = g.avatar_url_as(format="jpg")
        base = f"https://api.popcatdev.repl.co/welcomecard?background=https://media.discordapp.net/attachments/827137926491144215/861188219411103744/aaaaa.png&text1={one}&text2={two}&text3={three}&avatar={avatar}"
        await channel.send(base)
    except:
        pass


@client.event
async def on_raw_message_delete(payload):
    try:
        channelID = payload.channel_id
        cha = payload.cached_message
        author = cha.author
        msg = cha.content
        await client.snipe.replace_one({'_id': str(channelID)}, {'_id': str(channelID),"message":str(msg),"author":str(author)}, True)
        chan = client.get_channel(862572754347622432)
        embedVar = discord.Embed(title = "delete log" , color = discord.Colour.gold())
        embedVar.set_thumbnail(url = author.avatar_url)
        embedVar.add_field(name = "message",value = f"{msg}",inline = False)
        embedVar.add_field(name = "where",value = f"{channelID}",inline = False)
        await chan.send(embed = embedVar)
    except:
        pass

@client.event
async def on_raw_reaction_add(payload):
    emojiID = payload.emoji.id
    try:
        info = await client.rr.find_one({'_id': str(payload.message_id)})
        if str(emojiID) == info["emojiID"]:
            mem = payload.member
            gu = await client.fetch_guild(payload.guild_id)
            role = discord.Guild.get_role(gu,int(info["roleID"]))
            await mem.add_roles(role)
            return
    except :
        pass

@client.command()
@commands.is_owner()
async def load(ctx : Context , extention):
    client.load_extension(f'cogs.{extention}')

@client.command()
@commands.is_owner()
async def unload(ctx : Context , extention):
    client.unload_extension(f'cogs.{extention}')
  


@client.command(aliases = ["ANIME","ANIMEMEME"])
@commands.cooldown(rate=1,per=15)
async def animeme(ctx : Context):
    try:
        sr = await reddit.subreddit("Animemes")
        st = await sr.random()
        if not st.is_self: 
            slink = st.url
        await ctx.channel.send(slink)
    except:
        await ctx.channel.send("didnt find anything")
    return

@animeme.error
async def define_error(ctx:Context ,error):
    await ctx.channel.send(error)
    return

@client.command(aliases = ["MEME"])
@commands.cooldown(rate=1,per=15)
async def meme(ctx : Context):
    try:
        sr = await reddit.subreddit("Memes")
        st = await sr.random()
        if not st.is_self:  # We only want to work with link posts
            slink = st.url
        await ctx.channel.send(slink)
    except:
        await ctx.channel.send("didnt find anything")
    return

@meme.error
async def define_error(ctx:Context ,error):
    await ctx.channel.send(error)
    return

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_message(message: discord.Message):
    mention = f'<@!{client.user.id}>'
    if mention in message.content:
        prefix_json = open("prefix.json", "r")
        js = json.load(prefix_json)
        try:
            await message.channel.send("hi there my prefix is \"{0}\" use \"{0}help\" to know some commands".format(js[f"{message.guild.id}"]))
        except:
            await message.channel.send("hi there my prefix is \"chan \" use \"chan help\" to know some commands")
    await client.process_commands(message)


client.run("token goes here")

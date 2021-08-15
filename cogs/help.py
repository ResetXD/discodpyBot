import discord
from discord.ext import commands
from discord.ext.commands.context import Context

class Help(commands.Cog):

    def __init__(self,client):
        self.client = client
        self.client.help_command = None

    @commands.command(aliases = ['bothelp'])
    async def help(self,ctx:Context,helpWhat = None):
        a = await ctx.author.create_dm()
        if helpWhat == None:
            embedVar = discord.Embed(title = "help" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "Moderation" , value = "purge,ban,unban,kick,\nnickname,giverole,warn,dm",inline = False)
            embedVar.add_field(name = "Fun",value = "amongus,meme,animeme,choice,\nroll,avatar,8ball,ree,rps,comic",inline = False)
            embedVar.add_field(name = "image",value = "blurpify,magik,trash,stickbug,deepfry,\neko,owo,ph,tweet,loli,\n,kanna,clyde,fact,changemymind",inline = False)
            embedVar.add_field(name = "economy",value = "acc,beg,bet,give",inline = False)
            embedVar.add_field(name = "tv",value = "anime,manga,anisearch,mangasearch,aninum,manum",inline = False)
            embedVar.add_field(name = "music(no help for them)",value = "play(yt link or name only),stop,fuckoff,pause,queue,resume",inline = False)
            embedVar.add_field(name = "nsfw",value = "nhentai,hkitsune,nhentai,readnhentai,rule34",inline = False)
            embedVar.add_field(name = "osu",value = "osu,recent",inline = False)
            embedVar.add_field(name = "Utility",value = "serverinfo,whoami,\ndeletechannel,createchannel,\nroles,setwelcome",inline = False)
            embedVar.add_field(name = "Support",value = "owner,invite,server",inline = False)
            embedVar.set_footer(text = "type \"chan help <command name>\" for more info")
            await a.send("cause of addding new commands and increase in commands it would become spam in discord channel hope you understand")
            await a.send(embed = embedVar)
            return
        
        if helpWhat in ['rule34','34','r34']:
            embedVar = discord.Embed(title = "RULE34" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "rule34,34,r34(i guess not sure)",inline = False)
            embedVar.add_field(name = "permissions" , value = "nsfw channel marked",inline = False)
            embedVar.add_field(name = "what it does" , value = "just as rule34 suggest if there something which can get lewd it will get lewd",inline = False)
            embedVar.add_field(name = "developer 's note" , value = "rule34 is a bit ...meh just be carefull",inline = False)
            embedVar.add_field(name = "another developer 's note" , value = "not every time you will get what u wanted if you repeat the same character a new image will come rather than the old one",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <name(anime character you want to lewd)>\"")
            await ctx.channel.send(embed = embedVar)
            return

        
        if helpWhat in ['readnhentai','rh']:
            embedVar = discord.Embed(title = "READNHENTAI" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "readnhentai,rh",inline = False)
            embedVar.add_field(name = "permissions" , value = "nsfw channel marked",inline = False)
            embedVar.add_field(name = "what it does" , value = "give pages of the book in the specific range",inline = False)
            embedVar.add_field(name = "developer 's note" , value = "look man of culture this command looks a bit difficult\nbut just understand it properly to read some good book directly on dc if your brain cant undertand it then read the example",inline = False)
            embedVar.add_field(name = "example" , value = "chan hentai <media_id> -> pages starting from 1 to 10\nes hentai <media_id> 10 ->pages starting from 10 to +10\nes hentai <media_id> 10 24 -> pages starting from 10 to 24\nNOTE: when u use chan nhentai <id> it also gives the number of pages if the range is over that then it will just send useless links",inline = False)
            embedVar.add_field(name = "another developer 's note" , value = "look... you can get all the pages all at once but WHY WOULD YOU DO THAT, RIGHT?",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <media_id(chan hentai <id> to get this) <starting_range> <ending_range>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['nhentai']:
            embedVar = discord.Embed(title = "NHENTAI" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "nhentai",inline = False)
            embedVar.add_field(name = "permissions" , value = "nsfw channel marked",inline = False)
            embedVar.add_field(name = "what it does" , value = "search nhentai code and gives info about it",inline = False)
            embedVar.add_field(name = "developer 's note" , value = "you need to use this command before \"chan rh\" for media_id also i see you are a man of culture",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <code>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['nhentai']:
            embedVar = discord.Embed(title = "NHENTAI" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "nhentai",inline = False)
            embedVar.add_field(name = "permissions" , value = "nsfw channel marked",inline = False)
            embedVar.add_field(name = "what it does" , value = "search nhentai code and gives info about it",inline = False)
            embedVar.add_field(name = "developer 's note" , value = "you need to use this command before \"chan rh\" for media_id",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <code>\"")
            await ctx.channel.send(embed = embedVar)
            return

        if helpWhat in ['amongus','amoungus']:
            embedVar = discord.Embed(title = "AMONGUS" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "amoungus,amongus",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "a random amoung us gif",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias>\"")
            await ctx.channel.send(embed = embedVar)
            return  
        
        if helpWhat in ['Support',"support","invite","server","inv"]:
            await ctx.invoke(self.client.get_command('invite'))
            return  
        
        if helpWhat in ['nsfw','NSFW']:
            embedVar = discord.Embed(title = "NSFW" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "permissions" , value = "channel need to be nsfw marked",inline = False)
            embedVar.add_field(name = "commands" , value = "nhentai,hkitsune,nhentai,readnhentai,rule34",inline = False)
            embedVar.add_field(name = "developer 's note" , value = "i am a big weeb so expect more commands on hentai soon <:smart:829057265653907466>",inline = False)
            embedVar.set_footer(text = "MoreHelp - \"chan help <command_name>\"")
            await ctx.channel.send(embed = embedVar)
            return 
        
        if helpWhat in ['music','MUSIC']:
            embedVar = discord.Embed(title = "MUSIC" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "permissions" , value = "0 for users",inline = False)
            embedVar.add_field(name = "commands" , value = "AS I SAID NO HELP ~~not like i cant make it but more like i am lazy~~",inline = False)
            embedVar.set_footer(text = "MoreHelp - \"chan help <command_name>\"")
            await ctx.channel.send(embed = embedVar)
            return 

        if helpWhat in ['economy',"eco"]:
            embedVar = discord.Embed(title = "ECONOMY" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "permissions" , value = "0 for users",inline = False)
            embedVar.add_field(name = "commands" , value = "acc,bet,beg,give",inline = False)
            embedVar.set_footer(text = "MoreHelp - \"chan help <command_name>\"")
            await ctx.channel.send(embed = embedVar)
            return   

        if helpWhat in ['image']:
            embedVar = discord.Embed(title = "IMAGE" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "permissions" , value = "0 for users",inline = False)
            embedVar.add_field(name = "commands" , value = "blurpify,magik,trash,stickbug,deepfry,\nhentai,hkitsune,neko,owo,ph,tweet,loli",inline = False)
            embedVar.set_footer(text = "MoreHelp - \"chan help <command_name>\"")
            await ctx.channel.send(embed = embedVar)
            return   
        
        if helpWhat in ['Utility',"utility"]:
            embedVar = discord.Embed(title = "UTILITY" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "permissions" , value = "permissions varies with different commands",inline = False)
            embedVar.add_field(name = "commands" , value = "serverinfo,whoami,\ndeletechannel,createchannel,roles",inline = False)
            embedVar.set_footer(text = "MoreHelp - \"chan help <command_name>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['stickbug']:
            embedVar = discord.Embed(title = "stickbug" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "stickbug",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "stickbug user avatar with mp4",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <@someone/ID>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['acc','account']:
            embedVar = discord.Embed(title = "ACCOUNT" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "acc,account",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "to create or check account data",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <@someone/ID(optional)>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['beg']:
            embedVar = discord.Embed(title = "BEG" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "beg",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "beg for moni",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['bet']:
            embedVar = discord.Embed(title = "BET" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "bet",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "bet your moni away cause no other way to send moni rn",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <how much to bet>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['give','giv','givmoni']:
            embedVar = discord.Embed(title = "GIVE" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "giv,givmoni,give",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "give your moni to someone else",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <@someone/ID> <how much to give>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['trash']:
            embedVar = discord.Embed(title = "trash" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "trash",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "trash user avatar",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <@someone/ID>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['warn','w','w+']:
            embedVar = discord.Embed(title = "WARN" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "warn,w+,w",inline = False)
            embedVar.add_field(name = "permissions" , value = "kick_member",inline = False)
            embedVar.add_field(name = "what it does" , value = "warn a person by 1",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <@someone/ID> <reason(not important)>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['removewarn','rw','w-']:
            embedVar = discord.Embed(title = "REMOVEWARN" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "removewarn,w-,rw",inline = False)
            embedVar.add_field(name = "permissions" , value = "kick_member",inline = False)
            embedVar.add_field(name = "what it does" , value = "remove warn of a person by 1",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <@someone/ID> <reason(not important)>\"")
            await ctx.channel.send(embed = embedVar)
            return


        if helpWhat in ['osu',"osu!"]:
            embedVar = discord.Embed(title = "osu!" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "permissions" , value = "0 for users",inline = False)
            embedVar.add_field(name = "commands" , value = "osu,recent",inline = False)
            embedVar.set_footer(text = "MoreHelp - \"chan help <command_name>\"")
            await ctx.channel.send(embed = embedVar)
            return

        if helpWhat in ['tv',"TV"]:
            embedVar = discord.Embed(title = "ANIME" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "permissions" , value = "0 for users",inline = False)
            embedVar.add_field(name = "commands" , value = "anime,manga,anisearch,mangasearch,aninum,manum",inline = False)
            embedVar.set_footer(text = "MoreHelp - \"chan help <command_name>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['animenum','aninum']:
            embedVar = discord.Embed(title = "ANIMENUM" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "animenum,aninum",inline = False)
            embedVar.add_field(name = "permissions" , value = "0 for users",inline = False)
            embedVar.add_field(name = "what it does" , value = "sometimes u get the wrong anime from chan anime so use this command to check the next anime in that list",inline = False)
            embedVar.add_field(name = "example" , value = "chan aninum 1 noragami -> will not return the first result as first can be optained by -> chan ani noragami and/or chan aninum 0 noragami",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <position(default=0)> <anime name>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['manganum','manum']:
            embedVar = discord.Embed(title = "MANGANUM" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "manganum,manum",inline = False)
            embedVar.add_field(name = "permissions" , value = "0 for users",inline = False)
            embedVar.add_field(name = "what it does" , value = "sometimes u get the wrong manga from chan manga so use this command to check the next manga in that list",inline = False)
            embedVar.add_field(name = "example" , value = "chan manum 1 noragami -> will not return the first result as first can be optained by -> chan manum noragami and/or chan manum 0 noragami",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <position(default=0)> <manum name>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['mangasearch','ms']:
            embedVar = discord.Embed(title = "MANGASEARCH" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "mangasearch,ms",inline = False)
            embedVar.add_field(name = "permissions" , value = "0 for users",inline = False)
            embedVar.add_field(name = "what it does" , value = "search manga from mal api",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <manga name>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['animesearch','as']:
            embedVar = discord.Embed(title = "ANIMESEARCH" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "aniemsearch,as",inline = False)
            embedVar.add_field(name = "permissions" , value = "0 for users",inline = False)
            embedVar.add_field(name = "what it does" , value = "search anime from mal api",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <anime name>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['anime','ani']:
            embedVar = discord.Embed(title = "ANIME" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "anime,ani",inline = False)
            embedVar.add_field(name = "permissions" , value = "0 for users",inline = False)
            embedVar.add_field(name = "what it does" , value = "info on anime from mal api",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <anime name>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['manga']:
            embedVar = discord.Embed(title = "MANGA" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "manga",inline = False)
            embedVar.add_field(name = "permissions" , value = "0 for users",inline = False)
            embedVar.add_field(name = "what it does" , value = "info on manga from mal api",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <manga name>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        
        
        if helpWhat in ['Fun',"fun","entertainment"]:
            embedVar = discord.Embed(title = "FUN" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "permissions" , value = "0 for users",inline = False)
            embedVar.add_field(name = "commands" , value = "meme,animeme,choice,\nroll,avatar,8ball,ree,rps",inline = False)
            embedVar.set_footer(text = "MoreHelp - \"chan help <command_name>\"")
            await ctx.channel.send(embed = embedVar)
            return

        if helpWhat in ['Moderation',"mod","moderation"]:
            embedVar = discord.Embed(title = "MODERATION" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "permissions" , value = "permissions varies with different commands",inline = False)
            embedVar.add_field(name = "commands" , value = "purge,ban,unban,kick,\nnickname,giverole,warn,removewarn,dm",inline = False)
            embedVar.set_footer(text = "MoreHelp - \"chan help <command_name>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        
        if helpWhat in ['purge','clear','clean','bulkremove','vanish']:
            embedVar = discord.Embed(title = "PURGE" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "purge,clear,clean,bulkremove,vanish",inline = False)
            embedVar.add_field(name = "permissions" , value = "manage messages",inline = False)
            embedVar.add_field(name = "what it does" , value = "clear/remove/bulk delete messages",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <no of messages>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['blurpify']:
            embedVar = discord.Embed(title = "blurpify" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "blurpify,Blurpify",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "blurpify the user avatar",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <@someone/ID>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['ph','phcomment']:
            embedVar = discord.Embed(title = "phcomment" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "ph,phcomment",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "ph comment",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <@someone/ID> <text>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['dm']:
            embedVar = discord.Embed(title = "DM" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "dm",inline = False)
            embedVar.add_field(name = "permissions" , value = "adminstrator",inline = False)
            embedVar.add_field(name = "what it does" , value = "message the mentioned user",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <@someone/ID> <message>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['deepfry']:
            embedVar = discord.Embed(title = "deepfry" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "deepfry",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "deepfry avatar",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <@someone/ID>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['loli','lolice']:
            embedVar = discord.Embed(title = "loli" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "loli,lolice",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "lolice avatar",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <text>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['clyde','botsay']:
            embedVar = discord.Embed(title = "clyde" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "clyde,botsay",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "clyde say stuff",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <text>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['kanna','say']:
            embedVar = discord.Embed(title = "kanna" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "kanna,say",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "kanna say stuff",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <text>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['fact']:
            embedVar = discord.Embed(title = "fact" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "fact",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "the truth of the world",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <text>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['changemymind','change']:
            embedVar = discord.Embed(title = "changemymind" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "changemymind,change",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "i cant change your mind smh",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <text>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['hentai','Hentai']:
            embedVar = discord.Embed(title = "HENTAI" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "hentai,Hentai",inline = False)
            embedVar.add_field(name = "permissions" , value = "nsfwChannel and 0",inline = False)
            embedVar.add_field(name = "what it does" , value = "i see you are a man of culture",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias>\"")
            await ctx.channel.send(embed = embedVar)
            return

        if helpWhat in ['hkitsune']:
            embedVar = discord.Embed(title = "hkitsune" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "hkitsune",inline = False)
            embedVar.add_field(name = "permissions" , value = "nsfwChannel and 0",inline = False)
            embedVar.add_field(name = "what it does" , value = "i see you are a man of culture",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['magik']:
            embedVar = discord.Embed(title = "magik" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "magik",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "magik user avatar",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <@someone/ID>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['neko','catgirl']:
            embedVar = discord.Embed(title = "neko" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "neko,catgirl",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "catgirl uwu",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['owo']:
            embedVar = discord.Embed(title = "OwO" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "owo",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "owo",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <@someone/ID>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['setwelcome']:
            embedVar = discord.Embed(title = "SETWELCOME" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "setwelcome",inline = False)
            embedVar.add_field(name = "permissions" , value = "administrator",inline = False)
            embedVar.add_field(name = "what it does" , value = "set a welcome channel with unique message",inline = False)
            embedVar.add_field(name = "note" , value = "the welcome message will always have @new_member first",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <#channel> <unique message>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['roles','listroles']:
            embedVar = discord.Embed(title = "ROLES" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "roles,listroles",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "list roles in that server from lowest to highest",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['comic']:
            embedVar = discord.Embed(title = "COMIC" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "comic",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "comic from my favorite artist xkcd",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['giverole','addrole','gr']:
            embedVar = discord.Embed(title = "GIVEROLE" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "gr,giverole,addrole",inline = False)
            embedVar.add_field(name = "permissions" , value = "manage roles",inline = False)
            embedVar.add_field(name = "what it does" , value = "gives roles",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <role_name/@role> <@who/ID>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['ani']:
            embedVar = discord.Embed(title = "ANI" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "ani",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "finds the anime from mal(takes a bit of time)",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <anime name to search>\"")
            await ctx.channel.send(embed = embedVar)
            return
        if helpWhat in ['manga']:
            embedVar = discord.Embed(title = "MANGA" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "manga",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "finds the manga from mal(takes a bit of time)",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <manga name to search>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['osu','osuuser']:
            embedVar = discord.Embed(title = "osu user" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "osu,osuuser",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "sends info about the osu username",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <osu-username>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['recent','r','recentplay','osurecent']:
            embedVar = discord.Embed(title = "RECENT PLAY" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "recent,r, recentplay, osurecent",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "sends info about the osu username 's recent play",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <osu-username>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['top','t','topplay','osutop']:
            embedVar = discord.Embed(title = "TOP PLAY" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "top,t,topplay,osutop",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "sends info about the osu username 's top 10 play",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <osu-username>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['meme']:
            embedVar = discord.Embed(title = "MEMES" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "meme",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "shows a meme from r/Memes",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['animeme','anime']:
            embedVar = discord.Embed(title = "MEMES" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "animeme,anime",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "shows a meme from r/Animememes",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['rand','random','roll','randomint']:
            embedVar = discord.Embed(title = "ROLL" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "rand,random,roll,randomint",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "roll a random number for u",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <start(optional default-0)> <end(optional)>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['whoami','whois','me','ui','aboutme']:
            embedVar = discord.Embed(title = "WHOAMI/WHOIS" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "whoami,whois,me,ui,aboutme",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "gives a genral info about u in the specific guild",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <ID or ping(optional for yourself)>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['choice','pick','po','whichone']:
            embedVar = discord.Embed(title = "CHOICE" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "choice,pick,po,whichone",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "picks a random str from the given input",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <any number of choices seprated with space>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['dc','deletechannel']:
            embedVar = discord.Embed(title = "DELETECHANNEL" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "dc,deletechannel",inline = False)
            embedVar.add_field(name = "permissions" , value = "manage channels",inline = False)
            embedVar.add_field(name = "what it does" , value = "deletes the channel specified",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <channel ID> <reason>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['cc','createchannel']:
            embedVar = discord.Embed(title = "CREATECHANNEL" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "cc,createchannel",inline = False)
            embedVar.add_field(name = "permissions" , value = "manage channels",inline = False)
            embedVar.add_field(name = "what it does" , value = "creates a channel in the same category",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <channel ID to copy users perms from> <new channel name>\"")
            await ctx.channel.send(embed = embedVar)
            return

        if helpWhat in ['ban','removeunban']:
            embedVar = discord.Embed(title = "BAN" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "ban,removeunban",inline = False)
            embedVar.add_field(name = "permissions" , value = "ban members",inline = False)
            embedVar.add_field(name = "what it does" , value = "ban the person till the end of the world",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <ping the user> <reason>\"")
            await ctx.channel.send(embed = embedVar)
            return

        if helpWhat in ['unban','removeban']:
            embedVar = discord.Embed(title = "UNBAN" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "unban,removeban",inline = False)
            embedVar.add_field(name = "permissions" , value = "ban members",inline = False)
            embedVar.add_field(name = "what it does" , value = "unban the person",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <ping the lucky user>\"")
            await ctx.channel.send(embed = embedVar)
            return

        if helpWhat == "kick":
            embedVar = discord.Embed(title = "KICK" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "kick",inline = False)
            embedVar.add_field(name = "permissions" , value = "kick members",inline = False)
            embedVar.add_field(name = "what it does" , value = "kick the person from the guild",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <ping the user> <reason>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['av','avatar','pfp']:
            embedVar = discord.Embed(title = "AVATAR" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "av,avatar,pfp",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "shows the users profile picture",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <ping the user or use ID >\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['_8ball','8ball','8b']:
            embedVar = discord.Embed(title = "8BALL" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "_8ball,8ball,8b",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "always tells the truth unless hes high",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <question you want to ask>\"")
            await ctx.channel.send(embed = embedVar)
            return

        if helpWhat == "ree":
            await ctx.channel.send("https://tenor.com/view/reeeeeeeeeeeeeeeeee-gif-19312523")
            return
        
        if helpWhat in ['rps','rockpaperscissorshoot']:
            embedVar = discord.Embed(title = "RPS" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "rps,rockpaperscissorshoot",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "simple rock paper scissor game",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <your answer i.e. rock/paper/siccor>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['tweet','twitter']:
            embedVar = discord.Embed(title = "TWEET" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "tweet,twitter",inline = False)
            embedVar.add_field(name = "permissions" , value = "0",inline = False)
            embedVar.add_field(name = "what it does" , value = "tweet!",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <@someone/ID> <text>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ["nick","nickname"]:
            embedVar = discord.Embed(title = "NICKNAME" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "alias" , value = "nick,nickname",inline = False)
            embedVar.add_field(name = "permissions" , value = "manage nicknames",inline = False)
            embedVar.add_field(name = "what it does" , value = "changes the nickname of user",inline = False)
            embedVar.set_footer(text = "Format - \"chan <alias> <user ping or ID> <nickname>\"")
            await ctx.channel.send(embed = embedVar)
            return
        
        if helpWhat in ['register']:
            embedVar = discord.Embed(title = "register" , color = discord.Colour.dark_theme())
            embedVar.set_thumbnail(url = self.client.user.avatar_url)
            embedVar.add_field(name = "developer 's note" , value = "only can be used once think carefully or be like me and pick wizard",inline = False)
            embedVar.add_field(name = "developer 's second note" , value = "if you dont understand how this works then use \"chan docs\" ~~yes there is a docs~~",inline = False)
            embedVar.add_field(name = "archer" , value = "-less HP\n-less mana",inline = True)
            embedVar.add_field(name = "thief" , value = "-less HP\n-less mana",inline = True)
            embedVar.add_field(name = "assassin" , value = "-less HP\n-less mana",inline = True)
            embedVar.add_field(name = "ranger" , value = "-less HP\n-less mana",inline = True)

            embedVar.add_field(name = "priest" , value = "-average HP\n-high mana",inline = True)
            embedVar.add_field(name = "dark priest" , value = "-average HP\n-very high mana",inline = True)

            embedVar.add_field(name = "wizard" , value = "-average HP\n-very high mana and healing",inline = True)
            embedVar.add_field(name = "magic item craftsman" , value = "-low HP\n-very high mana",inline = True)
            embedVar.add_field(name = "adventurer" , value = "-low HP\n-very low mana\n-can become anything if done properly",inline = True)
            embedVar.set_footer(text = "Format - \"chan register <class>\"")
            await ctx.channel.send(embed = embedVar)
            return

    @help.error
    async def help_error(self, ctx:Context ,error):
        await ctx.channel.send(error)
        return


def setup(client):
    client.add_cog(Help(client))
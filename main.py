import discord
import random
import akinator as ak
import asyncio
import xkcd
import joke_generator
import os
import json
from itertools import cycle
from discord.ext.commands import CommandNotFound
from ruamel.yaml import YAML
from discord.ext import commands, tasks
from keep_alive import keep_alive
from pyrandmeme import *
import randfacts

client = commands.Bot(command_prefix="|")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='your commands | Type |help to view commands'))
    print("Bot is ready")
@client.command()
async def fine(ctx):
	await ctx.send('great')
@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True )
async def clear(ctx,amount=2):
	await ctx.channel.purge(limit = amount)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True )
async def kick(ctx,member : discord.Member,*,reason= "No reason provided"):
	await member.send("You have been kicked from the server, Because:"+reason)
	await member.kick(reason=reason)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True )
async def ban(ctx,member : discord.Member,*,reason= "No reason provided"):
	await member.send("You have been banned from the server, Because:"+reason)
	await member.ban(reason=reason)
@client.command()
async def car(ctx):
            responses = [
                f"https://tenor.com/view/lamborghini-car-sports-car-luxury-car-lamborghini-aventador-gif-4633234?",
                f"https://tenor.com/view/lamborghini-cars-lambo-gif-11950646",
                f"https://tenor.com/view/lamborghini-aventador-supercar-car-lp700-gif-12251184",
                f"https://tenor.com/view/fast-street-racing-muscle-car-race-car-cars-gif-4550935",
                f"https://tenor.com/view/car-fast-car-luxury-car-sports-car-aston-martin-gif-4633243",
            ]
            await ctx.send(random.choice(responses))
@client.command()
async def nickname(ctx):
            responses = [
                f"loser",
                f"dumbdumb",
                f"cool boi",
                f"big fishy",
            ]
            await ctx.send(random.choice(responses))

@client.command()
async def name(ctx) :
    await ctx.send ("My name is {0.user}".format(client))
@client.command()
async def fortuneball(ctx):
            responses = [
                f"As I see it, yes",
                f"Ask again later",
                f"Better not tell you now",
                f"Cannot predict now",
                f"Concentrate and ask again",
                f"Don't count on it",
                f"It is certain",
                f"It is decidedly so",
            ]
            await ctx.send(random.choice(responses))
@client.command()
async def advice(ctx):
            responses = [
                f"A faithful friend is a strong defense.",
                f"A fresh start will put you on your way.",
                f"A golden egg of opportunity falls into your lap this month.",
                f"A friend asks only for your time not your money",
                f"A light heart carries you through all the hard times.",
                f"A smile is your personal welcome mat.",
                f"A smooth long journey! Great expectations",
                f"An inch of time is an inch of gold.",
                f"Any decision you have to make tomorrow is a good decision.",
                f"At the touch of love, everyone becomes a poet.",
                f"Believe in yourself and others will too.",
                f"An acquaintance of the past will affect you in the near future.",
                f"All your hard work will soon pay off.",
                f"An important person will offer you support.",
                f"All will go well with your new project.",
                f"Allow compassion to guide your decisions.",
                f"Curiosity kills boredom. Nothing can kill curiosity.",
                f"Dedicate yourself with a calm mind to the task at hand.",
                f"Depart not from the path which fate has you assigned.",
                f"Determination is what you need now.",
                f"Carve your name on your heart and not on marble",
                f"Disbelief destroys the magic.",
                f"Do not be intimidated by the eloquence of others.",
                f"Distance yourself from the vain.",
                f"Do not demand for someone’s soul if you already got his heart.",
                f"Do not make extra work for yourself.",
                f"Do not underestimate yourself. Human beings have unlimited potentials.",
                f"Don’t just spend time. Invest it.",
                f"Don’t just think, act!",
                f"Don’t let your limitations overshadow your talents.",
                f"Emulate what you admire in your parents.",
                f"Every wise man started out by asking many questions.",
                f"Everyday in your life is a special occasion.",
                f"Education is the ability to meet life’s situations",
                f"Failure is the path of lease persistence",
                f"Failure is the path of lease persistence.",
                f"Fear and desire – two sides of the same coin.",
                f"For hate is never conquered by hate. Hate is conquered by love.",
                f"Expect much of yourself and little of others.",
                f"Fearless courage is the foundation of victory.",
                f"For the things we have to learn before we can do them, we learn by doing them.",
                f"From now on your kindness will lead you to success.",
                f"Get your mind set – confidence will lead you on.",
                f"From listening comes wisdom and from speaking repentance.",
                f"Good to begin well, better to end well.",
                f"Happiness begins with facing life with a smile and a wink.",
                f"If you continually give, you will continually have",
                f"Like the river flow into the sea. Something are just meant to be.",
                f"It is better to deal with problems before they arise.",
                f"Keep your face to the sunshine and you will never see shadows.",
                f"In the end all things will be known.",

            ]
            await ctx.send(random.choice(responses))
@client.command()
async def yesno(ctx):
            responses = [
                f"https://entsecarch.files.wordpress.com/2014/08/yes.jpg",
                f"https://miro.medium.com/max/620/0*mzvBo2d5dQMX3UVi.jpg",
            ]
            await ctx.send(random.choice(responses))
@client.command()
async def wouldyourather(ctx):
            responses = [
                f"https://i.ytimg.com/vi/8-tNnGErKKo/maxresdefault.jpg",
                f"https://img.playbuzz.com/image/upload/ar_1.5,c_pad,f_jpg,b_auto/cdn/d038db53-6eb4-4cc7-93c4-95a30523dbc1/0da388ba-69c3-4d1d-805b-5d1a32efcdb2.jpg",
                f"https://images-na.ssl-images-amazon.com/images/I/71E0otI+JVL.jpg",
                f"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9u8kA-yxSWJDPreYJjFHX8IIMrF_SJLV5ag&usqp=CAU",
                f"https://i.ytimg.com/vi/U2MHUuUE79M/hqdefault.jpg",
                f"https://i.kym-cdn.com/photos/images/masonry/001/239/719/9ea.png",
                f"https://i1.wp.com/www.wouldyourathermath.com/wp-content/uploads/2017/08/WYR-Exponents.jpg?ssl=1",
                f"https://pbs.twimg.com/media/CFWl06yWEAAVy4-.png",
                f"https://pbs.twimg.com/media/D66WgjmW4AA1jMk.jpg",
            ]
            await ctx.send(random.choice(responses))

client.remove_command("help")
@client.group(invoke_without_command=True)
async def help(ctx):
	em = discord.Embed(title = "Help", description = "Use |help <command> for extended information on a command.",color = ctx.author.color)

	em.add_field(name = "Moderation", value= "`kick`, `ban`, `message`,`Server`")
	em.add_field(name = "Fun", value = "`fortuneball`, `meme`, `nickname`, `yesno`, `wouldyourather`,`car`,`cat`,`dog`,`beg`,`mandolorian`,`joke`,`Advice`,`Akinator`,`dp`,`comic`,`whois`,`Giveaway`,`fact`")
	await ctx.send(embed = em)
@help.command()
async def kick(ctx):
	em = discord.Embed(title = "Kick", description = "Kicks a member from the server", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|kick @member [reason]")
	await ctx.send(embed = em)
@help.command()
async def whois(ctx):
    em = discord.Embed(title = "Whois", description = "Gives info about a user", color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "|whois")
    await ctx.send(embed = em)
@help.command()
async def giveaway(ctx):
    em = discord.Embed(title = "Giveaway", description = "Makes giveaways", color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "|giveaway")
    await ctx.send(embed = em)
@help.command()
async def fact(ctx):
    em = discord.Embed(title = "Fact", description = "Sends facts", color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "|server")
    await ctx.send(embed = em)
@help.command()
async def server(ctx):
    em = discord.Embed(title = "Server", description = "Sends server info", color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "|server")
    await ctx.send(embed = em)
@help.command()
async def dp(ctx):
    em = discord.Embed(title = "Server", description = "Sends profile pic of the person you mentioned", color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "|getdp")
    await ctx.send(embed = em)
@help.command()
async def comic(ctx):
    em = discord.Embed(title = "Server", description = "Sends comics", color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "|comic")
    await ctx.send(embed = em)
@help.command()
async def akinator(ctx):
	em = discord.Embed(title = "Akinator", description = "Creates a akinator game", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|akinator")
	await ctx.send(embed = em)
@help.command()
async def factr(ctx):
	em = discord.Embed(title = "Akinator", description = "Sends some fact", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|fact or |rfact")
	await ctx.send(embed = em)


@help.command()
async def ban(ctx):
	em = discord.Embed(title = "Ban", description = "Bans a member from the server", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|ban @member| [reason]")
	await ctx.send(embed = em)
@help.command()
async def message(ctx):
	em = discord.Embed(title = "Message", description = "Delete's message", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|clear 2")
	await ctx.send(embed = em)

@help.command()
async def meme(ctx):
	em = discord.Embed(title = "Meme", description = "Posts meme's", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|meme")
	await ctx.send(embed = em)

@help.command()
async def advice(ctx):
	em = discord.Embed(title = "Advice", description = "Gives some advice", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|advice")
	await ctx.send(embed = em)
@help.command()
async def fortuneball(ctx):
	em = discord.Embed(title = "Fortune ball", description = "Tells fortune", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|fortuneball")
	await ctx.send(embed = em)
@help.command()
async def nickname(ctx):
	em = discord.Embed(title = "Nickname", description = "Gives you a nickname", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|nickname")
	await ctx.send(embed = em)
@help.command()
async def yesno(ctx):
	em = discord.Embed(title = "Yes/no", description = "Tells whether yes or no", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|yesno")
	await ctx.send(embed = em)
@help.command()
async def wouldyourather(ctx):
	em = discord.Embed(title = "Would you Rather", description = "Gives you some would you rather questions", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|wouldyourather")
	await ctx.send(embed = em)
@help.command()
async def beg(ctx):
	em = discord.Embed(title = "Beg", description = "Will give you some money", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|beg")
	await ctx.send(embed = em)
@help.command()
async def car(ctx):
	em = discord.Embed(title = "Car", description = "Sends some car gif", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|car")
	await ctx.send(embed = em)
@help.command()
async def cat(ctx):
	em = discord.Embed(title = "Cat", description = "Sends some cat gif", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|cat")
	await ctx.send(embed = em)
@help.command()
async def dog(ctx):
	em = discord.Embed(title = "Dog", description = "Sends some Dog gif", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|Dog")
	await ctx.send(embed = em)
@help.command()
async def mandolorian(ctx):
	em = discord.Embed(title = "Mandolorian", description = "Sends some Mandolorian gif", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|mandolorian")
	await ctx.send(embed = em)
@help.command()
async def joke(ctx):
	em = discord.Embed(title = "Joke", description = "sends some jokes", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|joke")
	await ctx.send(embed = em)

@help.command()
async def join(ctx):
	em = discord.Embed(title = "Join", description = "sends invite to the Server", color = ctx.author.color)
	em.add_field(name = "**Syntax**", value = "|join")
	await ctx.send(embed = em)
@client.command()
async def cat(ctx):
	responses = [
	f"https://tenor.com/view/cute-kitty-best-kitty-alex-cute-pp-kitty-omg-yay-cute-kitty-munchkin-kitten-gif-15917800",
	f"https://tenor.com/view/nyancat-pusheen-gif-8723100",
	f"https://tenor.com/view/shummer-netflix-cat-cute-gif-12702077",
	f"https://media4.giphy.com/media/H4DjXQXamtTiIuCcRU/giphy.gif",
	f"https://tenor.com/view/cat-love-huge-hug-big-gif-11990658",
	f"https://tenor.com/view/catface-gif-4351869",
	f"https://tenor.com/view/good-morning-funny-animals-insomnia-cat-tired-crazy-cute-gif-11458685",
	f"https://i.pinimg.com/originals/c3/2b/fa/c32bfa16bcf864e478d3ddfe32440268.gif",
	f"https://media0.giphy.com/media/3o6Zt481isNVuQI1l6/200.gif",
	f"https://res.cloudinary.com/jerrick/image/upload/fl_progressive,q_auto,w_1024/teqcyxcn1hboqpuwifcq.gif",
	f"https://sweetytextmessages.com/wp-content/uploads/2018/02/Funny-Cat-Gifs-for-Laugh-2.gif",
	f"https://media1.giphy.com/media/yFQ0ywscgobJK/giphy.gif",
	f"https://i.pinimg.com/originals/13/f2/02/13f2029ef55cd645217d5df463c9e874.gif",
	f"https://i.pinimg.com/originals/8f/46/c5/8f46c58eb5ef0f59bced2f795d5dfde2.gif",
	f"https://i.pinimg.com/originals/90/21/3b/90213b075aa367086bfe687750827baf.gif",
	f"https://i.pinimg.com/originals/8f/46/c5/8f46c58eb5ef0f59bced2f795d5dfde2.gif",
	f"https://media.tenor.com/images/1baa5a8d48673742bb1d1dc0dcc2b4cc/tenor.gif",
	f"https://data.whicdn.com/images/224162445/original.gif",
	f"https://3.bp.blogspot.com/-qJrED1Dk890/Ul5rrklcKvI/AAAAAAAAtsI/w6LU6kgXMAw/s1600/funny-cats-gifs-073-007.gif",
	f"https://i1.wp.com/media.tenor.com/images/bb33cc1eaafa266ac1092ecff7c1c85d/tenor.gif",
	]
	await ctx.send(random.choice(responses))
@client.command()
async def dog(ctx):
	responses = [
	f"https://tenor.com/view/relax-chill-dog-cute-swing-gif-16656710",
	f"https://media.tenor.com/images/4636fb297bf682bc57c68e3acc66b80a/tenor.gif",
	f"https://post.barkbox.com/wp-content/uploads/2013/02/tumblr_mbl5larwCV1qdoqhwo1_500.gif",
	f"https://media2.giphy.com/media/82nrkDUHJCMiA/giphy.gif",
	f"https://thumbs.gfycat.com/HandsomeClassicAfricangoldencat-max-1mb.gif",
	f"https://i.pinimg.com/originals/86/51/d7/8651d7ed34abda66015b4950e2e96ddb.gif",
	f"https://townsquare.media/site/341/files/2013/04/Cutest-Dogs1.gif",
	f"https://media.tenor.com/images/cdfed1a6dcf16a9b1f84b21cdac076c4/tenor.gif",
	f"https://post.barkbox.com/wp-content/uploads/2013/02/tumblr_mf39gmuHjZ1rccyxzo1_500.gif",
	f"https://cdn140.picsart.com/307143055075201.gif?to=min&r=640",
	f"https://thumbs.gfycat.com/FlamboyantTenderKitfox-max-1mb.gif",
	f"https://media3.giphy.com/media/Xf7yfCbS1aZwi4WqGn/giphy.gif",
	f"http://onwardstate.com/wp-content/uploads/2015/05/cute.gif",
	]
	await ctx.send(random.choice(responses))
@client.command()
async def mandolorian(ctx):
	responses = [
	f"https://tenor.com/view/mandalorian-whatcha-doin-gif-15656494",
	f"https://thumbs.gfycat.com/ForthrightShabbyAnkole-size_restricted.gif",
	f"https://tenor.com/view/mando-way-this-is-the-way-mandalorian-star-wars-gif-18467370",
	f"https://tenor.com/view/baby-yoda-baby-yoda-happy-laughing-smile-happy-gif-16061896",
	f"https://tenor.com/view/baby-yoda-star-wars-mandalorian-eating-egg-gif-19171092",
	f"https://tenor.com/view/baby-yoda-drink-sip-blink-the-mandalorian-gif-15693643",
	f"https://tenor.com/view/this-is-the-way-mandalorian-this-is-the-way-intensifies-gif-16048235",
	f"https://tenor.com/view/the-mandalorian-the-child-star-wars-baby-yoda-cute-gif-16181684",
	f"https://tenor.com/view/cobb-vanth-the-mandalorian-its-gonna-be-great-star-wars-timothy-olyphant-gif-19005468",
	f"https://tenor.com/view/the-mandalorian-cobb-vanth-star-wars-work-something-out-maybe-we-can-work-something-out-gif-19003770",
	f"https://i.pinimg.com/originals/b3/e9/1f/b3e91ff096b62c849d3491b1f5fef6d5.gif",
	]
	await ctx.send(random.choice(responses))
@client.command(aliases=["getprofilepic","dp"])
async def getdp(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    await ctx.send(member.avatar_url)
@client.command(aliases=["xkcd"])
async def comic(ctx, user : discord.Member =None):
    async with ctx.typing():
        if not user:
            user=ctx.author
        await ctx.send("Here's your comic "+user.mention)
        url = xkcd.Comic.getImageLink(xkcd.getRandomComic())
        await ctx.send(url)
@client.event
async def on_member_join(member):
    await client.send_message(f"""WELCOME TO THE SERVER {member.mention}""")

@client.command()
async def server(ctx):
    name=str(ctx.guild.name)
    description=str(ctx.guild.description)
    owner=str(ctx.guild.owner)
    _id = str(ctx.guild.id)
    region=str(ctx.guild.region)
    memcount=str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)

    embed=discord.Embed(
        title=name +" Server Information",
        description=description,
        color=discord.Color.blue()
        )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner",value=owner,inline=True)
    embed.add_field(name="Server Id",value=_id,inline=True)
    embed.add_field(name="Region",value=region,inline=True)
    embed.add_field(name="Member Count",value=memcount,inline=True)

    await ctx.send(embed=embed)
@client.command(aliases=["hi"])
async def sup(ctx, member : discord.Member = None):
    if not member:
        member = ctx.author
    await ctx.send('Hello! '+member.mention)
@client.command(aliases=["aki"])
async def akinator(ctx):
    intro=discord.Embed(title="Akinator",description="Hello, "+ctx.author.mention+"I am Akinator!!!",color=discord.Colour.blue())
    intro.set_thumbnail(url="https://en.akinator.com/bundles/elokencesite/images/akinator.png?v93")
    intro.set_footer(text="Think about a real or fictional character. I will try to guess who it is")
    bye=discord.Embed(title="Akinator",description="Bye, "+ctx.author.mention,color=discord.Colour.blue())
    bye.set_footer(text="Akinator left the chat!!")
    bye.set_thumbnail(url="https://i.pinimg.com/originals/28/fc/0b/28fc0b88d8ded3bb8f89cb23b3e9aa7b.png")
    await ctx.send(embed=intro)
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["y", "n","p","b","yes","no","probably","idk","back"]
    try:
        aki = ak.Akinator()
        q = aki.start_game()
        while aki.progression <= 80:
            question=discord.Embed(title="Question",description=q,color=discord.Colour.blue())
            ques=["https://i.imgflip.com/uojn8.jpg","https://ih1.redbubble.net/image.297680471.0027/flat,750x1000,075,f.u1.jpg"]
            question.set_thumbnail(url=ques[random.randint(0,1)])
            question.set_footer(text="Your answer:(y/n/p/idk/b)")
            question_sent=await ctx.send(embed=question)
            try:
                msg = await client.wait_for("message", check=check , timeout=30)
            except asyncio.TimeoutError:
                await question_sent.delete()
                await ctx.send("Sorry you took too long to respond!(waited for 30sec)")
                await ctx.send(embed=bye)
                return
            await question_sent.delete()
            if msg.content.lower() in ["b","back"]:
                try:
                    q=aki.back()
                except ak.CantGoBackAnyFurther:
                    await ctx.send(e)
                    continue
            else:
                try:
                    q = aki.answer(msg.content.lower())
                except ak.InvalidAnswerError as e:
                    await ctx.send(e)
                    continue
        aki.win()
        answer=discord.Embed(title=aki.first_guess['name'],description=aki.first_guess['description'],color=discord.Colour.blue())
        answer.set_thumbnail(url=aki.first_guess['absolute_picture_path'])
        answer.set_image(url=aki.first_guess['absolute_picture_path'])
        answer.set_footer(text="Was I correct?(y/n)")
        await ctx.send(embed=answer)
        #await ctx.send(f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct?(y/n)\n{aki.first_guess['absolute_picture_path']}\n\t")
        try:
            correct = await client.wait_for("message", check=check ,timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("Sorry you took too long to respond!(waited for 30sec)")
            await ctx.send(embed=bye)
            return
        if correct.content.lower() == "y":
            yes=discord.Embed(title="Yeah!!!",color=discord.Colour.blue())
            yes.set_thumbnail(url="https://i.pinimg.com/originals/ae/aa/d7/aeaad720bd3c42b095c9a6788ac2df9a.png")
            await ctx.send(embed=yes)
        else:
            no=discord.Embed(title="Oh Noooooo!!!",color=discord.Colour.blue())
            no.set_thumbnail(url="https://i.pinimg.com/originals/0a/8c/12/0a8c1218eeaadf5cfe90140e32558e64.png")
            await ctx.send(embed=no)
        await ctx.send(embed=bye)
    except Exception as e:
        await ctx.send(e)
@client.command(aliases=["info","details"])
async def whois(ctx, member : discord.Member = None):
    if not member:
        member = ctx.author
    embed=discord.Embed(title=member.name,description=member.mention,color=discord.Colour.blue())
    embed.add_field(name="ID",value=member.id,inline=False)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)

@client.command()
async def meme(ctx):
    await ctx.send(embed=await pyrandmeme())

mainshop = [{"name":"Watch","price":100,"description":"Time"},
            {"name":"Laptop","price":1000,"description":"Work"},
            {"name":"PC","price":10000,"description":"Gaming"},
            {"name":"Ferrari","price":99999,"description":"Sports Car"}]

@client.command(aliases=['bal'])
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f'{ctx.author.name} Balance',color = discord.Color.red())
    em.add_field(name="Wallet Balance", value=wallet_amt)
    em.add_field(name='Bank Balance',value=bank_amt)
    await ctx.send(embed= em)

@client.command()
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(f'{ctx.author.mention} Got {earnings} coins!!')

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)


@client.command(aliases=['wd'])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,'bank')
    await ctx.send(f'{ctx.author.mention} You withdrew {amount} coins')


@client.command()
async def deposit(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,'bank')
    await ctx.send(f'{ctx.author.mention} You deposited {amount} coins')


@client.command(aliases=['sm'])
async def send(ctx,member : discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount,'bank')
    await update_bank(member,amount,'bank')
    await ctx.send(f'{ctx.author.mention} You gave {member} {amount} coins')


@client.command(aliases=['rb'])
async def rob(ctx,member : discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)


    if bal[0]<100:
        await ctx.send('It is useless to rob him :(')
        return

    earning = random.randrange(0,bal[0])

    await update_bank(ctx.author,earning)
    await update_bank(member,-1*earning)
    await ctx.send(f'{ctx.author.mention} You robbed {member} and got {earning} coins')


@client.command()
async def slots(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return
    final = []
    for i in range(3):
        a = random.choice(['X','O','Q'])

        final.append(a)

    await ctx.send(str(final))

    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        await update_bank(ctx.author,2*amount)
        await ctx.send(f'You won :) {ctx.author.mention}')
    else:
        await update_bank(ctx.author,-1*amount)
        await ctx.send(f'You lose :( {ctx.author.mention}')


@client.command()
async def shop(ctx):
    em = discord.Embed(title = "Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f"${price} | {desc}")

    await ctx.send(embed = em)



@client.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return


    await ctx.send(f"You just bought {amount} {item}")


@client.command()
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = "Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)    

    await ctx.send(embed = em)


async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]
    

@client.command()
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    await ctx.send(f"You just sold {amount} {item}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.7* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]


@client.command(aliases = ["lb"])
async def leaderboard(ctx,x = 1):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)


async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open('mainbank.json','w') as f:
        json.dump(users,f)

    return True


async def get_bank_data():
    with open('mainbank.json','r') as f:
        users = json.load(f)

    return users


async def update_bank(user,change=0,mode = 'wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('mainbank.json','w') as f:
        json.dump(users,f)
    bal = users[str(user.id)]['wallet'],users[str(user.id)]['bank']
    return bal



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
yaml = YAML()

with open("./config.yml", "r", encoding="utf-8") as file:
    config = yaml.load(file)
def convert(time):
    pos = ["s", "m", "h", "d", "w"]
    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24, "w": 3600 * 24 * 7}
    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


@client.command()
@commands.has_role(config['giveaway_role'])
async def giveaway(ctx):

    timeout = config["setup_timeout"]
    embedq1 = discord.Embed(title="<a:gw:822331085873610762> | Giveaway", description=f"Welcome to the Giveaway. Answer the following questions within ``{timeout}`` Seconds!")
    embedq1.add_field(name=":star: | Question 1", value="Where should we host the Giveaway?\n\n **Example**: ``#General``")
    embedq2 = discord.Embed(title="<a:gw:822331085873610762>| Giveaway", description="Great! Let's move onto the next question.")
    embedq2.add_field(name=":star: | Question 2", value="How long should it last? ``<s|m|h|d|w>``\n\n **Example**:\n ``1d``")
    embedq3 = discord.Embed(title="<a:gw:822331085873610762>  | Giveaway", description="Awesome. You've made it to the last question!")
    embedq3.add_field(name=":star: | Question 2", value="What is the prize the winner will receive?\n\n **Example**:\n ``1 million``")

    questions = [embedq1,
                 embedq2,
                 embedq3]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for i in questions:
        await ctx.send(embed=i)

        try:
            msg = await client.wait_for('message', timeout=config['setup_timeout'], check=check)
        except asyncio.TimeoutError:
            embed = discord.Embed(title="<a:gw:822331085873610762> **Giveaway **", description=":x: You didn't answer in time!")
            await ctx.send(embed=embed)
            return
        else:
            answers.append(msg.content)

    try:
        c_id = int(answers[0][2: -1])
    except:
        embed = discord.Embed(title=":tada: **Giveaway **", description=":x: You didn't specify a channel correctly!")
        await ctx.send(embed=embed)
        return

    channel = client.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        embed = discord.Embed(title=":tada: **Giveaway**", description=":x: You didn't set a proper time unit!")
        await ctx.send(embed=embed)
        return
    elif time == -2:
        embed = discord.Embed(title=":tada: **Giveaway **", description=":x: Time unit **MUST** be an integer")
        await ctx.send(embed=embed)
        return
    prize = answers[2]

    embed = discord.Embed(title=":tada: **Giveawayd**", description="Okay, all set. The Giveaway will now begin!")
    embed.add_field(name="Hosted Channel:", value=f"{channel.mention}")
    embed.add_field(name="Time:", value=f"{answers[1]}")
    embed.add_field(name="Prize:", value=prize)
    await ctx.send(embed=embed)
    print(f"New Giveaway Started! Hosted By: {ctx.author.mention} | Hosted Channel: {channel.mention} | Time: {answers[1]} | Prize: {prize}")
    print("------")
    embed = discord.Embed(title=f"**{prize}**", description=f"React With {config['react_emoji']} To Participate!", color=0xf1c40f)
    embed.add_field(name="Lasts:", value=answers[1])
    embed.add_field(name=f"Hosted By:", value=ctx.author.mention)
    msg = await channel.send(embed=embed)

    await msg.add_reaction(config['react_emoji'])
    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(msg.id)
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)
    if config['ping_winner_message'] == True:
        await channel.send(f":confetti_ball: Congratulations! {winner.mention} you won the **{prize}**!")
        print(f"New Winner! User: {winner.mention} | Prize: {prize}")
        print("------")

    embed2 = discord.Embed(title=f"**{prize}**", description=f":trophy: **Winner:** {winner.mention}",colour = 0xe74c3c)
    embed2.set_footer(text="Giveaway Has Ended")
    await msg.edit(embed=embed2)


@client.command()
@commands.has_role(config['giveaway_role'])
async def reroll(ctx, channel: discord.TextChannel, id_: int):
    try:
        new_msg = await channel.fetch_message(id_)
    except:
        prefix = config['prefix']
        await ctx.send(f"Incorrect usage! Do: `{prefix}reroll <Channel Name - Must be the channel which previously held the giveaway> <messageID of the giveaway message>` ")

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await ctx.channel.send(f":confetti_ball: The new winner is: {winner.mention}!")
@client.command(aliases=["rfact"])
async def fact(ctx):
    await ctx.send(randfacts.getFact())
@client.command()
async def joke(ctx):
    await ctx.send(joke_generator.generate())
keep_alive()
client.run(os.getenv('TOKEN')) 

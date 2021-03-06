import discord
import random
import asyncio
import os
from discord.ext import commands

class Fun(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['8ball'])
  async def _8ball(self, ctx, *, question):
    Responses = [" It is certain.",
                 "It is decidedly so.",
                    "Without a doubt.",
                 "Yes – definitely.",
                   "You may rely on it.",
                  "As I see it, yes.",
                   "Most likely.",
                  "Outlook good.",
                  "Yes.",
                  "Signs point to yes.",
                 "Could you shut up?",
                 "Ask again later.",
                   "Better not tell you now.",
                   "Cannot predict now.",
                   "Concentrate and ask again.",
                  "Do not count on it.",
                  "My reply is no.",
                  "My sources say no.",
                    "Outlook not so good.",
                 "Very doubtful.",
                  "Shut it Buster",
                  "Why are you even asking me",
                    "Come another time.",
                 "REEEEEEEEEEEEEEEEEEEEEE"]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(Responses)}')

  @_8ball.error
  async def _8ball_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("What's the question?")

  @commands.command()
  async def dankrate(self, ctx, member: discord.Member=None):
    if member == None:
      member = ctx.author
    dankrate_response = [f"{member.name}'s dankrate is {random.randint(1, 30)}% :sweat:", f"{member.name}'s dankrate is {random.randint(31, 50)}% :eyes:", f"{member.name}'s dankrate is {random.randint(51, 70)}% :pensive:", f"{member.name}'s dankrate is {random.randint(71, 90)}% :star_struck:", f"{member.name}'s dankrate is {random.randint(91, 100)}% :sunglasses:"]
    await ctx.send(random.choice(dankrate_response))

  @dankrate.error
  async def dankrater_error(self, ctx, error):
    if isinstance(error, commands.BadArgument):
      await ctx.send('Couldnt find the user. If the user has a space in their name use "<name>". EG- {prefix}dankrate "WILLY WONKA"')
      
  @commands.command()
  async def simprate(self, ctx, member: discord.Member=None):
    if member == None:
       member = ctx.author
    simprate_response = [f"{member.name}'s simprate is {random.randint(1, 30)}% :sweat:", f"{member.name}'s simprate is {random.randint(31, 50)}% :eyes:", f"{member.name}'s simprate is {random.randint(51, 70)}% :pensive:", f"{member.name}'s simprate is {random.randint(71, 90)}% :star_struck:", f"{member.name}'s simprate is {random.randint(91, 100)}% :sunglasses:"]
    await ctx.send(random.choice(simprate_response))

  @simprate.error
  async def simprate_error(self, ctx, error):
    if isinstance(error, commands.BadArgument):
      await ctx.send('Couldnt find the user. If the user has a space in their name use "<name>". EG- {prefix}simprate "WILLY WONKA"')

  @commands.command(aliases=["waifu"])
  async def waifurate(self, ctx, member: discord.Member=None):
    if member == None:
        member = ctx.author
    waifurate_response = [f"{member.name}'s {random.randint(1,30)}% waifu :face_vomiting:",f" {member.name}'s {random.randint(31, 50)}% waifu :tired_face:", f"{member.name}'s {random.randint(51, 70)}% waifu :grimacing:", f"{member.name}'s {random.randint(71, 90)}% waifu :smirk:", f"{member.name}'s {random.randint(91, 100)}% waifu :sunglasses:"]
    await ctx.send(random.choice(waifurate_response))
        
  @waifurate.error
  async def waifurate_error(self, ctx, error):
    if isinstance(error, commands.BadArgument):
      await ctx.send('Couldnt find the user. If the user has a space in their name use "<name>". EG- {prefix}waifurate "WILLY WONKA"')

  @commands.command(aliases=["lenny"])
  async def nny(self, ctx):
    await ctx.send("( ͡° ͜ʖ ͡°)")

  @commands.command()
  async def kill(self, ctx, member: discord.Member):
    if {member.name} == {ctx.author.name}:
        await ctx.send(f"Lets not do that {ctx.author.name}")
        return
    else:
      kill_response = [f'{member.name} died of cringe',
     f'{member.name} got hit by a canonball',
    f'{member.name} got drunk and decided to jump of the cliff',
    f'{member.name} got shot in the head',
    f'{member.name} got into a fight with the Pope. {member.name} is going to hell',
    f'{member.name} swallowed a rock',
    f'{member.name} died of watching T-Series',
    f'{member.name} became a hitman but got killed by his target instead. {member.name} is a failure.',
    f'{member.name} got rickrolled.',
    f'{member.name} dies due to lack of friends',
    f'{member.name} fell down a cliff while playing pokemon go']
    await ctx.send(f'{random.choice(kill_response)}')

  @kill.error
  async def kill_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("Who do you want me to... take out?")
    else:
      if isinstance(error, commands.BadArgument):
        await ctx.send("I cant kill someone who doesnt exist.")

  @commands.command()
  async def roast(self, ctx, member: discord.Member):
    roast_response = ['You’re the reason God created the middle finger.',
    'You are more disappointing than an unsalted pretzel.',
    'I forgot the world revolves around you. My apologies, how silly of me.',
    'Your face makes onions cry.',
    'I cant wait to forget you',
    'Take my lowest prioirty and put yourself beneath it',
    "You're like a square blade, all edge no point",
    'You have a face made for radio.',
    "Dont play hard to get when you're hard to want",
    'Just because your head is shaped like a light bulb, doesnt mean you have good ideas',
    f'There will never be enough middle fingers for you in the world {member.name}',
    "Your identity is more confusing than the Japanese alphabet's",
    "When you die, people will struggle to say nice things about you",
    "People like you are the reson god doesnt talk to use anymore",
    "You're as useless as 'ay' in okay",
    "If laughter is the best medicine, you're face must be curing the world"]
    await ctx.send(f'{random.choice(roast_response)}')

  @roast.error
  async def roast_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("Who gonna get the burn?")
    else:
      if isinstance(error,commands.BadArgument):
        await ctx.send("Mention a real person. Not your imaginary friend")

  @commands.command(aliases=['hack','HACK'])
  async def Hack(self,ctx, member : discord.Member):
    if {member.name} == {ctx.author.name}:
      await ctx.send(f"How do you hack yourself")
    else:
      message = await ctx.send(f" Hacking {member.name} right now chief")
      await asyncio.sleep(2)
      await message.edit(content=f"Fetching IP adress")
      await asyncio.sleep(2)
      await message.edit(content=f"IP found 182.110.224.90")
      await asyncio.sleep(2)
      await message.edit(content=f"Fetching Email and Password")
      await asyncio.sleep(2)
      hack_response_email = [f'{member.name}sucks@gmail.com',
      f'{member.name}hasnofriends@gmail.com']
      hack_response_password = ['iliketseries',
      'forgotten',
      'whyarewestillhere']
      await message.edit(content=f"**Email:** {random.choice(hack_response_email)}\n**Password:** {random.choice(hack_response_password)}")
      await asyncio.sleep(2)
      hack_Response_tabs = ['animehentai.com',
      "reddit.com",
      "useless.com",
      "howtogetfriends.com"]
      await message.edit(content=f"Fetching recently closed tabs")
      await asyncio.sleep(2)
      await message.edit(content=f"{random.choice(hack_Response_tabs)}")
      await asyncio.sleep(2)
      await message.edit(content=f"Trojan Injected")
      await asyncio.sleep(2)
      await message.edit(content=f"Hack completed chief")

  @Hack.error
  async def hack_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("Who do you want me to hack?")
    else:
      if isinstance(error, commands.BadArgument):
        await ctx.send("Hacking them right now cheif... Oh wait, you didnt mention a real person.")



def setup(bot):
  bot.add_cog(Fun(bot))
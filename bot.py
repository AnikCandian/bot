import discord
import random

from discord.ext import commands
from discord.ext.commands import has_permissions

bot = commands.Bot(command_prefix = "-")
messageIds = []
lcommands = [["ping", "Returns the time required for the host to send info about the bot to the server. Measured in milliseconds.", "ping", "ping"],
["passport", "Makes a request for you to get a passport.", "passport <Reason of Entry (string)>", "passport @The Immigration Officer#9428"],
["kick", "Kicks the requested player out of the group. Requires admin.", "kick <@Player (player)>", "kick @The Immigration Officer#9428"],
["setup", "Changes the bot's savings.", "setup <Option (string)> <Input (depends on Option)>", "setup prefix ;"],
["say", "Makes the bot say something.", "say <Text (string)>","say I'm a cookoo head."],
["flip", "Flips a coin and returns the outcome.", "flip", "flip"]
]

bot.remove_command('help')

@bot.event
async def on_ready():
	print("bot")
	await bot.change_presence(activity=discord.Game(name='a game called life'))

@bot.event
async def on_raw_reaction_add(payload):
	print("hola amigo")
	for messageId in messageIds:
		print(messageId)
		if messageId[0] == payload.message_id:
			print("Woah, " + str(messageId[1]) + " is cool.")
			#test = discord.utils.get(messageId[1].guild.roles, name="passport holder")
			#await messageId[1].add_roles(663674541842628608, messageId[1].id, 663695321351847946) #id: 663695321351847946
			test = discord.utils.get(messageId[1].guild.roles, name="passport holder")
			await messageId[1].add_roles(test)
			embed = discord.Embed(name="Passport Granted", description="You have been granted your passport. You may now access the channels of The Deep Zone!", color=0x7CFC00)
			await messageId[1].send(embed=embed)
			messageId = None

@bot.command(pass_context=True)
async def ping(ctx):
	await ctx.send(f"PONG! A humble {round(bot.latency * 1000)}ms!")

@bot.command(pass_context=True)
async def passport(ctx, *, reasonOfEntry):
	if ctx.message.channel.id == 663677327863185418:
		test = discord.utils.get(ctx.author.guild.roles, name="passport holder")
		if test in ctx.author.roles:
			await ctx.send("Doesn't look like you need a passport. You already have one!")
		else:
			await ctx.send("Thank you " + str(ctx.message.author) + " for applying for a passport. Please wait while a HR accepts your request.")
			channel = bot.get_channel(663805939249578007)
			embed = discord.Embed(title="Passport Request")
			embed.add_field(name="Name of Requestor:", value=ctx.message.author, inline=True)
			embed.add_field(name="Reason of Entry:", value=reasonOfEntry)
			message = await channel.send(embed=embed)
			print(message.id)
			messageIds.append([message.id, ctx.message.author])
	else:
		await ctx.send(str(ctx.message.author) + ", you are in the wrong channel. Go to #immigration.")

@has_permissions(administrator=True)
@bot.command(pass_context=True)
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)

@bot.command(pass_context=True)
@has_permissions(administrator=True)
async def setup(ctx, command, input):
	if command == "prefix":
		bot.command_prefix = input
		embed = discord.Embed(title="Action Finished!", description="The prefix has been changed to " + input, color=0x7CFC00)
		embed.add_field(name="Note", value="The prefix will reset whenever this bot gets restarted", inline=True)
		await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def say(ctx, *, whatToSay):
	await ctx.send(whatToSay)


@setup.error
async def setup_error(ctx, error):
	#if isinstance(error, MissingPermissions):
	embed = discord.Embed(title="Error", description="Something wrong happened. Please check if your command syntax was correct.", color=0xDC143C)
	await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def flip(ctx):
	outcome = random.choice([1,2])
	if outcome == 1:
		emoji = discord.utils.get(ctx.author.guild.emojis, name='heads')
		await ctx.send(emoji)
		await ctx.send("Heads!")
	else:
		emoji = discord.utils.get(ctx.author.guild.emojis, name="tails")
		await ctx.send(emoji)
		await ctx.send("Tails!")

@bot.command(pass_context=True)
async def help(ctx, command="None"):
	embed = None
	for a in lcommands:
		embed = discord.Embed(title=a[0], description=a[1], color=0x000FFF)
		check = a[0].find(command)
		if check != -1:
			embed.add_field(name="Syntax:", value=a[2], inline=True)
			embed.add_field(name="Example:", value=a[3], inline=True)
			break
		else:
			if command == "None":
				embed = discord.Embed(title="Help", description="Below are the commands you can use with me. For more information about each one, type in /help <command-name>", color=0x000FFF)
				for a in lcommands:
					embed.add_field(name=a[0], value=a[1], inline=False)
					#await ctx.send(embed=embed)
			else:
				embed = discord.Embed(title="Error", description="The command you searched for doesn't exist.", color=0xDC143C)
	await ctx.send(embed=embed)
	
@has_permissions(administrator=True)
@bot.command(pass_context=True)
async def warn(ctx, person, *, reason="None"):
	embed = discord.Embed(title="Warning", description="You have been warned by a Higher Up for breaking a rule.", color=0x00FF00)
	embed.add_field(name="Reason:", value=reason)
	embed.add_field(name="Warned by:", value=ctx.message.author)
	print(person)
	print(ctx.message.author)
	await person.send(embed=embed)
	await ctx.message.author.send(embed=embed)
	
@bot.command(pass_context=True)
async def pong(ctx):
	await ctx.send("@everyone")

bot.run("NjYzNjgzNTcwODA3NjAzMj" + "Iw.XhlI4Q.HhSN4NNCMt6eucmWAj00UokyGuo")

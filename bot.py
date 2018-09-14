import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

startup_ext = ["Music"]
bot = commands.Bot("$")

class Main_Commands():
	def __init__(self, bot):
		self.bot = bot

@bot.event
async def on_ready():
	print ("bot online!")

@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say("pong")

@bot.command(pass_context=True)
async def hello(ctx):
	await bot.say("Hi :wave: !!! ")


if __name__ == '__main__':
	for ext in startup_ext:
		try:
			bot.load_extension(ext)
		except:
			print ("Error while load %s" % ext)

bot.run("NDg4NjkzMDY5NjI2MDgxMjgw.DngNfQ.ZjOUliX3EjjSm_VgPTQ1f3HfsDk")
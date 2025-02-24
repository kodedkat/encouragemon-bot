import discord, random, datetime, pokemon_encouraging_messages
from discord.ext import commands
import time

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='/', intents=intents)

last_command_time = 0
# 3 seconds cooldown
cooldown_time = 3

@bot.event
async def on_ready():
  print(f'Logged on as {bot.user}!')
  await bot.sync_commands()

def random_message():
  return random.choice(pokemon_encouraging_messages.pokemon_encouraging_messages_list)

def get_encouraging_message():
  pokemon_encouraging_message = random_message()
  return pokemon_encouraging_message

@bot.slash_command(name="enmon", description="Catch an encouraging message from Pokémon")
async def encat_slash(ctx):
  global last_command_time

  current_time = time.time()
  if current_time - last_command_time < cooldown_time:
    await ctx.respond("Please wait a moment before using this poké-mand again.", ephemeral=True)
    return
  
  last_command_time = current_time
  message = get_encouraging_message()
  await ctx.respond(message)

bot.run('token')
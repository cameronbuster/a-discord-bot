import discord
from discord.ext import commands
from config import BOT_TOKEN
from commands import register_commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    await register_commands(bot)

    print("Ready!")


bot.run(BOT_TOKEN)

# filepath: discord-autism-bot/src/main.py

import discord
import asyncio

from discord import app_commands
from discord_utils.message_fetcher import fetch_recent_channel_messages, fetch_recent_user_messages
from llm.model import AutismModel
from config import CHANNEL_MESSAGE_HISTORY_LIMIT, USER_MESSAGE_HISTORY_LIMIT, DEV_GUILD_ID


COMMANDS_REGISTERED = False

async def register_commands(bot: discord.Client):
    
    # See if the commands are registered or not (On disconnect / sleep, will run into problems re-syncing already existing commands)
    global COMMANDS_REGISTERED
    if COMMANDS_REGISTERED:
        return
    COMMANDS_REGISTERED = True

    existing = await bot.tree.fetch_commands(guild=discord.Object(id=DEV_GUILD_ID))
    existing_names = {cmd.name for cmd in existing}

    tree = bot.tree

    @tree.command(name="measurechannelautism", description="Determine how autistic the channel is.", guild=discord.Object(id=DEV_GUILD_ID))
    @app_commands.describe(channel="The channel in question")
    async def channel_autism(interaction: discord.Interaction, channel: discord.TextChannel):
        
        # Pause the response to the interaction. Eventually respond to the interaction via the handler
        await interaction.response.defer()

        # Fetch the last x messages from the channel
        channel_messages = await fetch_recent_channel_messages(channel=channel, lookback=CHANNEL_MESSAGE_HISTORY_LIMIT)
        print(channel_messages)
        # Measure autism levels for the most recent messages in the channel
        autism_model = AutismModel()
        autism_calculation = await asyncio.gather(*(autism_model.measure_autism(msg) for msg in channel_messages))

        message = (f'{channel} autism calculation complete: {autism_calculation}')

        await interaction.followup.send(message)


    @tree.command(name="measureuserautism", description="Determine how autistic the user is.", guild=discord.Object(id=DEV_GUILD_ID))
    @app_commands.describe(username="The retard in question")
    async def user_autism(interaction: discord.Interaction, username: discord.User, channel: discord.TextChannel):
        
        # Pause the response to the interaction. Eventually respond to the interaction via the handler
        await interaction.response.defer()

        # Fetch the last x messages from the channel
        user_messages = await fetch_recent_user_messages(username=username, channel=channel, lookback=USER_MESSAGE_HISTORY_LIMIT)

        # Measure autism levels for the most recent messages in the channel
        autism_model = AutismModel()
        autism_calculation = await asyncio.gather(*(autism_model.measure_autism(msg.content) for msg in user_messages))

        message = (f'{user_autism} autism calculation complete: {autism_calculation}')

        await interaction.followup(message)

    # Force sync all commands to the Dev Guild
    synced = await tree.sync(guild=discord.Object(id=DEV_GUILD_ID))
    
    synced_names = {cmd.name for cmd in synced}
    new_names = synced_names - existing_names

    print(f'✅ Synced {len(new_names)} commands to Server (guild: {DEV_GUILD_ID})')

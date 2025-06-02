# filepath: discord-autism-bot/src/config.py
import os


API_KEY = os.getenv("DISCORD_BOT_API_KEY")
DEV_GUILD_ID = int(os.getenv("DEV_GUILD_ID"))
MODEL_NAME = "all-MiniLM-L6-v2"
CHANNEL_MESSAGE_HISTORY_LIMIT = 100  # Number of messages to analyze for channel-level autism
USER_MESSAGE_HISTORY_LIMIT = 100  # Number of messages to analyze for user-level autism
ACTIVE_USER_LIMIT = 10  # Number of most active users to calculate average autism level
AUTISM_THRESHOLD = 0.5  # Threshold for determining autism level significance
LOGGING_LEVEL = "INFO"  # Logging level for the bot's operation

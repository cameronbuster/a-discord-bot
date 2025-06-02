def fetch_recent_channel_messages(channel, lookback):
    """
    Fetches the last x number of messages from a specified Discord channel.

    Args:
        channel: The Discord channel to fetch messages from.
        limit: The number of messages to fetch.

    Returns:
        A list of messages fetched from the channel.
    """
    messages = channel.history(limit=lookback).flatten()
    return messages


def fetch_recent_user_messages(user, channel, lookback):
    """
    Fetches the last x number of messages from a specific user in a specified channel.

    Args:
        user: The Discord user whose messages are to be fetched.
        channel: The Discord channel to fetch messages from.
        limit: The number of messages to fetch.

    Returns:
        A list of messages from the user in the channel.
    """
    messages = channel.history(limit=lookback).flatten()
    user_messages = [msg for msg in messages if msg.author == user]
    return user_messages

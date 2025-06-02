# A Discord Bot

This project is a Discord bot that measures the "autism level" of channels users based on their last X number of messages. It utilizes a free open-source LLM model from HuggingFace and the SentenceTransformers library to analyze user messages and calculate autism levels.

## Features

- Measures autism levels based on user messages.
- Fetches messages from Discord channels and users.
- Utilizes an LLM model for message analysis.

## Project Structure

```
a-discord-bot
├── src
│   ├── main.py          # Entry point of the Discord bot
│   ├── bot.py           # Handles interactions with the Discord API
│   ├── llm
│   │   ├── model.py     # Initializes the LLM model and processes messages
│   │   └── utils.py     # Utility functions for message preprocessing
│   ├── discord_utils
│   │   ├── message_fetcher.py  # Fetches messages from Discord
│   └── config.py        # Configuration settings for the bot
├── requirements.txt      # Lists project dependencies
└── README.md             # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd a-discord-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Configure the bot settings in `src/config.py` (API keys, model parameters, etc.).
2. Run the bot:
   ```
   python src/main.py
   ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is open-source and available under the MIT License.
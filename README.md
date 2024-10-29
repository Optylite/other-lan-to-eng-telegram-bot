# other-lan-to-eng-telegram-bot
a telegram bot that translates other languages to English

# Telegram Translation Bot

This Telegram bot translates non-English messages into English using the `langdetect` library for language detection and `deep-translator` for translation. Built with Python and `python-telegram-bot`, this bot will automatically detect and translate text messages sent in languages other than English.

## Features

- Responds to the `/start` command with a welcome message.
- Detects the language of each text message.
- Translates non-English messages to English and sends the translated text back to the user.

## Prerequisites

- **Python 3.7+**
- **Telegram Bot Token**: You’ll need a token to connect your bot to Telegram. Get one from the [BotFather](https://core.telegram.org/bots#botfather).

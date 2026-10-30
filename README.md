# TP Editz — Telegram Group Management Bot

A modular Telegram group-management bot maintained by **TP Editz**.

This repository is a maintained fork of the original [MukeshRobot project](https://github.com/Noob-Mukesh/MukeshRobot). The upstream MIT license and original copyright notices are retained. TP Editz branding and maintenance changes are applied in this fork.

## Features

- Group administration and moderation commands
- User and chat management utilities
- Notes, rules, filters, and backup/restore modules
- Modular command structure
- Telegram integrations built with Pyrogram, Telethon, and python-telegram-bot

## Requirements

- Python version compatible with the pinned packages in `requirements.txt`
- Telegram API ID and API hash from [my.telegram.org](https://my.telegram.org/apps)
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- A MongoDB connection URI
- The environment variables documented in `app.json` and `MukeshRobot/config.py`

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/tpeditz/BestManagementbot.git
   cd BestManagementbot
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # Linux/macOS
   source .venv/bin/activate
   # Windows PowerShell
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Configure the required Telegram and database values using the configuration options in `MukeshRobot/config.py` or the environment variables listed in `app.json`. Never commit real API keys, bot tokens, or database credentials.

5. Start the bot:

   ```bash
   python -m MukeshRobot
   ```

## Important compatibility note

The Python package directory and import path are still named `MukeshRobot`. This is intentional: many modules, deployment commands, and existing installations depend on that identifier. Renaming it globally as part of a visual rebrand would break imports and deployment unless handled as a separate, fully tested migration.

## Project links

- Repository: [tpeditz/BestManagementbot](https://github.com/tpeditz/BestManagementbot)
- Maintainer: [TP Editz](https://github.com/tpeditz)
- Upstream source: [Noob-Mukesh/MukeshRobot](https://github.com/Noob-Mukesh/MukeshRobot)

## License and attribution

This project is distributed under the MIT License. The original upstream copyright and license notices remain in place. See [LICENSE](LICENSE) for the full terms.

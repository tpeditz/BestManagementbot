# TP Editz — Telegram Group Management Bot

**TP Editz** maintains this Telegram group-management bot fork.

This repository is based on the original [MukeshRobot project](https://github.com/Noob-Mukesh/MukeshRobot). It is a maintained fork, not a claim of authorship over the upstream code. Original MIT license and copyright notices are retained.

## Project

A modular Telegram bot with group administration, moderation, user utilities, notes, rules, filters, and backup/restore features.

## Requirements

- Python and the packages pinned in `requirements.txt`
- Telegram API ID and API hash from [my.telegram.org](https://my.telegram.org/apps)
- A bot token from [@BotFather](https://t.me/BotFather)
- A MongoDB connection URI
- The required configuration values listed in `app.json` and `MukeshRobot/config.py`

## Setup

Clone this repository:

```bash
git clone https://github.com/tpeditz/BestManagementbot.git
cd BestManagementbot
```

Create and activate a virtual environment:

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Set the required Telegram, owner, support-chat, start-image, and database values in your environment or in the configuration file. Never commit real API keys, bot tokens, or database credentials.

Start the bot:

```bash
python -m MukeshRobot
```

## Docker

The repository includes a Dockerfile. Build from the repository root:

```bash
docker build -t tp-editz-group-manager .
```

Supply your configuration securely through environment variables when running the container.

## Compatibility note

The Python package directory and import path remain named `MukeshRobot`. Existing modules, deployment commands, and stored database collections depend on those identifiers. They are deliberately not renamed as part of a branding-only change because doing so would require a coordinated migration and could break existing installations or data.

## Links

- **Repository:** [tpeditz/BestManagementbot](https://github.com/tpeditz/BestManagementbot)
- **Maintainer:** [TP Editz on GitHub](https://github.com/tpeditz)
- **Telegram:** [TP Editz](https://t.me/Tp_Editz)
- **Upstream project:** [Noob-Mukesh/MukeshRobot](https://github.com/Noob-Mukesh/MukeshRobot)

## License and attribution

Distributed under the MIT License. The upstream copyright and license notices remain in the repository. See [LICENSE](LICENSE) for the full terms.

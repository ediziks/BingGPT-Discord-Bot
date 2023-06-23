# BingGPT-Discord-Bot

BingGPT-Discord-Bot is a Discord bot that can be invited to any Discord servers and be interact with Microsoft's Bing Chat. It's on top of [https://github.com/acheong08/EdgeGPT](https://github.com/acheong08/EdgeGPT) reverse engineered API of Microsoft's Bing Chat which is currently running with GPT-4 and recently started to support Text-to-Image generation

## Setup

### Requirements

- python 3.8+
- A Microsoft Account with early access to <https://bing.com/chat> (Required)
- Docker (Optional: Preferred especially on Windows)

### Checking access (Required)

- Install the latest version of Microsoft Edge
- Alternatively, you can use any browser and set the user-agent to look like you're using Edge (e.g., `Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1474.0`). You can do this easily with an extension like "User-Agent Switcher and Manager" for [Chrome](https://chrome.google.com/webstore/detail/user-agent-switcher-and-m/bhchdcejhohfmigjafbampogmaanbfkg) and [Firefox](https://addons.mozilla.org/en-US/firefox/addon/user-agent-string-switcher/).
- Open [bing.com/chat](https://bing.com/chat)
- If you see a chat feature, you are good to go

### Getting authentication (Required)

- Install the cookie editor extension for [Chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) or [Firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)
- Go to `bing.com`
- Open the extension
- Click "Export" on the bottom right (This saves your cookies to clipboard)
- Paste your cookies into a file in the main folder named as `cookies.json`

### Installation & Running

1. Clone the repo and change directory to repo folder
   ```bash
   git clone https://github.com/ediziks/BingGPT-Discord-Bot.git
   cd BingGPT-Discord-Bot
   ```
2. Place `cookies.json` file into the main path. See [Getting authentication (Required)](https://github.com/ediziks/BingGPT-Discord-Bot#getting-authentication-required) section above for more information. Also, check `example.cookies.json` file to see the right path
3. Set the environment variables (`BOT_TOKEN` & `SERVER_ID`) in the `.env` file. See `.example.env` file to get the right format and the path. Check [creating Discord bot and getting the token](https://discordpy.readthedocs.io/en/stable/discord.html) for more details about the `BOT_TOKEN`. And, the `SERVER_ID` can be simply copied by right clicking the server logo you want to invite the bot, and selecting `COPY_ID`. See [how to get Discord server id](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID) for more information.
4. Install the requirements
   ```bash
   pip install -r requirements.txt
   ```
5. Make `bot.py` and `dcbot.sh` files executable
   ```bash
   chmod +x dcbot/bot.py dcbot.sh
   ```
6. The bot can be launched after completing the steps below. There are two alternatives to do so;
   - 1st method: Running the bot with python command in the terminal
     ```bash
     python dcbot/bot.py
     ```
   - 2nd method: Running the bot as a background process (Preferred)
     ```bash
     ./dcbot.sh
     ```
     - Bot logs can be find under `dcbot/bot.log`
     - Find the process id with the first command and stop the process by providing the process id in the second command
       ```bash
       ps ax | grep bot.py
       sudo kill -9 <proces_id>
       ```

### Installation & Running with Docker
1. Be sure that Docker and docker-compose are installed on your system
   - [Mac](https://docs.docker.com/docker-for-mac/install/)
   - [Linux](https://docs.docker.com/install/)
   - [Windows](https://docs.docker.com/docker-for-windows/install/)
2. Complete the installation section above up to 3th step (including the 3th)
2. Build the project
   ```bash
   docker-compose build
   ```
3. Run the application
   - Running in the shell/terminal  
     ```bash
     docker-compose up
     ```
   - Running in detached mode (similar as a background process)
     ```bash
     docker-compose up -d
     ```

### Inviting the Bot
See [how to invite a bot to Discord server](https://discordpy.readthedocs.io/en/stable/discord.html#inviting-your-bot) for more information about the bot invitation. Make sure that the bot permissions look like as in the image below before generating the invitation url

![invitation permissions](https://user-images.githubusercontent.com/54022220/229100554-0534ccd3-8318-4391-a5d4-ab057fc2a8ad.png)

## Usage
### Commands
```bash
/ask <prompt>      - Ask BingGPT a question
/imagine <prompt>  - Ask BingGPT to imagine visuals
/reset             - Reset the conversation
/hardreset         - Reset the session
```
### Sample Usage

![/ask usage](https://user-images.githubusercontent.com/54022220/229100391-c3e3c29a-4b4a-4a6f-9689-5ca41d8b4dcc.png)

![/imagine usage](https://user-images.githubusercontent.com/54022220/229100469-aa5813ff-fdb1-4dcc-bb2c-d115386ac04c.png)

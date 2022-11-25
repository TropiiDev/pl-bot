# pip install imports
import discord, aiofiles
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import asyncio 

# sys imports
import os 
import logging
import logging.handlers
import random

# local imports
import guildid

if os.path.exists('.\\databases\\snipe.json'):
    os.remove('.\\databases\\snipe.json')
    open('.\\databases\\snipe.json', "x")
    open('.\\databases\\snipe.json', "w").write("{}")
else:
    open('.\\databases\\snipe.json', "x")
    open('.\\databases\\snipe.json', "w").write("{}")

# check if discord.log exists if it does it deletes it than creates a new one
# if discord.log doesn't exist it creates a new one
# it is used to log errors
# it is also needed so the file doesnt get crammed with errors 
# its easier to understand when trying to look for errors in the code
if os.path.exists("discord.log"):
    os.remove("discord.log")
    open("discord.log", "x")
else:
    open("discord.log", "x")

# logging 
logger = logging.getLogger('discord')
logger.setLevel(logging.NOTSET)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

# startup stuff
load_dotenv()

# create the bot
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="-", intents=discord.Intents.all())
        self.synced = False
        self.warnings = {}
        self.remove_command("help")
        
    async def setup_hook(self):
        print(f'\33[32mLogged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_ready(self):
        await tree.sync(guild=guildid.guilds)
        self.synced = True
        

    async def load_extensions(self):
        for name in os.listdir('./commands'):
            if name.endswith('.py'):
                await self.load_extension(f'commands.{name[:-3]}')

    async def on_ready(self):
        for guild in self.guilds:
            async with aiofiles.open(f"{guild.id}.txt", mode="a") as temp:
                pass

            self.warnings[guild.id] = {}
        
        for guild in self.guilds:
            async with aiofiles.open(f"{guild.id}.txt", mode="r") as file:
                lines = await file.readlines()

                for line in lines:
                    data = line.split(" ")
                    member_id = int(data[0])
                    admin_id = int(data[0])
                    reason = " ".join(data[2:]).strip("\n")

                    try:
                        self.warnings[guild.id][member_id][0] += 1
                        self.warnings[guild.id][member_id][1].append((admin_id, reason))

                    except KeyError:
                        self.warnings[guild.id][member_id] = [1, [(admin_id, reason)]]
    
    async def on_guild_join(self, guild):
        self.warnings[guild.id] = {}

# making var for commands in this file
bot = MyBot()
tree = bot.tree

# start bot
async def main():
    async with bot:
        await bot.load_extensions()
        await bot.start(os.getenv("token"))
        await asyncio.sleep(0.1)
    await asyncio.sleep(0.1)

asyncio.run(main())
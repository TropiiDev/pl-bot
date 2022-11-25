import discord, guildid, json
from discord import app_commands
from discord.ext import commands

class snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Snipe Online")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        with open('.\\databases\\snipe.json', "r") as f:
            data = json.load(f)
        data[str(message.channel.id)] = {"author": str(message.author), "channel": str(message.channel.id), "content": str(message.content)}
        with open('.\\databases\\snipe.json', "w") as f:
            json.dump(data, f)
    
    @commands.hybrid_command(name="snipe", description="Sends the most recent deleted message")
    @app_commands.guilds(guildid.guilds)
    async def snipe(self, ctx, channel: discord.TextChannel=None):
        if channel == None:
            channel = ctx.channel
        with open('.\\databases\\snipe.json', "r") as f:
            data = json.load(f)
        try:
            author = data[str(channel.id)]["author"]
            content = data[str(channel.id)]["content"]
            channel = data[str(channel.id)]["channel"]
            await ctx.send(f"**{author}** said: '{content}' in <#{channel}>")
        except:
            await ctx.send("There is nothing to snipe")

async def setup(bot):
    await bot.add_cog(snipe(bot))
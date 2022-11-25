import discord, typing, guildid
from typing import Union
from discord import app_commands
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping Online")

    @commands.hybrid_command(name="ping", description="Pong!")
    @app_commands.guilds(guildid.guilds)
    async def ping(self, ctx):
        await ctx.send(f":ping_pong:**Pong!**\nLatency: {round(self.bot.latency * 1000)}ms")

async def setup(bot):
    await bot.add_cog(ping(bot))
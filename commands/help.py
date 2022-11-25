import discord, guildid
from discord import app_commands
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help Online")

    @commands.hybrid_command(name="help", description="Shows all commands")
    @app_commands.guilds(guildid.guilds)
    async def help(self, ctx):
        em = discord.Embed(title="Help", description="Shows all commands", color=ctx.author.color)
        em.add_field(name="Staff Commands", value="clear, kick, ban, mute, timeout, warn, giverole, setnick, snipe", inline=False)
        em.add_field(name="Normal Commands", value="help, ping, warnings, info, avatar, membercount, info, meme", inline=False)

        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(help(bot))
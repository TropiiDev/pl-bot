import discord, guildid
from discord import app_commands
from discord.ext import commands

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Info Online")

    @commands.hybrid_command(name="info", description="Shows info about the user")
    @app_commands.guilds(guildid.guilds)
    async def info(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author

        em = discord.Embed(title=f"{user.name}'s Info", description=f"Shows info about {user.name}", color=user.color)
        em.add_field(name="Name", value=user.name, inline=False)
        em.add_field(name="ID", value=user.id, inline=False)
        em.add_field(name="Status", value=user.status, inline=False)
        em.add_field(name="Top Role", value=user.top_role.mention, inline=False)
        em.add_field(name="Joined At", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        em.add_field(name="Created At", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        em.set_thumbnail(url=user.avatar)

        await ctx.send(embed=em)

async def setup(bot):
    await bot.add_cog(info(bot))
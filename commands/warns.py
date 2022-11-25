import discord, guildid, aiofiles
from discord import app_commands
from discord.ext import commands

class warns(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Warns Online")

    @commands.hybrid_command(name="warn", description="Warn a user")
    @app_commands.guilds(guildid.guilds)
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member:discord.Member, *, reason=None):
        # if member.id in [ctx.author.id, bot.user.id]:
        #    return await ctx.send("You cannot warn yourself or the bot!")

        if member is None:
            return await ctx.send("Please provide a member to warn")

        if reason is None:
            return await ctx.send("Please provide a reason for this warn")

        try:
            first_warning = False
            self.bot.warnings[ctx.guild.id][member.id][0] += 1
            self.bot.warnings[ctx.guild.id][member.id][1].append((ctx.author.id, reason))


        except KeyError:
            first_warning = True
            self.bot.warnings[ctx.guild.id][member.id] = [1, [(ctx.author.id, reason)]]
        count = self.bot.warnings[ctx.guild.id][member.id][0]

        async with aiofiles.open(f"{ctx.guild.id}.txt", mode="a") as file:
            await file.write(f"{member.id} {ctx.author.id} {reason}\n")

        await ctx.send(f"{member.mention} has {count} {'warning' if first_warning else 'warnings'}.")

    @commands.hybrid_command(name="warnings", description="Check a users warnings")
    @app_commands.guilds(guildid.guilds)
    async def warnings(self, ctx, member:discord.Member):
        if member is None:
            return await ctx.send("The provided member could not be found or you forgot to provide one.")

        em = discord.Embed(title=f"Displaying warnings for {member.name}", description="", color = ctx.author.color)
        try:
            i = 1
            for admin_id, reason in self.bot.warnings[ctx.guild.id][member.id][1]:
                admin = ctx.guild.get_member(admin_id)
                em.description += f"**Warning {i}** given by {admin.mention} for: '{reason}'.\n"
                i += 1

            await ctx.send(embed=em)

        except KeyError: # no warnings 
            nowarn = discord.Embed(title="", description="This user has no warnings.")
            await ctx.send(embed=nowarn)

async def setup(bot):
    await bot.add_cog(warns(bot))
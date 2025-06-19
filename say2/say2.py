import discord
from discord.ext import commands

class Say2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say2(self, ctx, *, message: str):
        """Sends a message to the channel."""
        for role in ctx.guild.roles:
            if role.name in message:
                message = message.replace(f"@{role.name}", role.mention)
        await ctx.send(
            message,
            allowed_mentions=discord.AllowedMentions(everyone=True, users=True, roles=True)
        )


async def setup(bot):
    await bot.add_cog(Say2(bot))

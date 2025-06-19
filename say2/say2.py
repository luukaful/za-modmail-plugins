import discord
from discord.ext import commands

class Say2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say2(self, ctx, *, message: commands.clean_content):
        """Sends a message to the channel."""
        await ctx.send(message)


async def setup(bot):
    await bot.add_cog(Say2(bot))

import discord
from discord.ext import commands

class Transfer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Dictionary to hold department channels'

        self.departments = {
            "mod": {
                "role_name": "Moderation Team",
                "category_id": 1385364595249647636,
                "role_id": 1385365202874405047
            },
            "pt": {
                "role_name": "Partnership Team",
                "category_id": 1385364686421360840,
                "role_id": 1385365283329544353
            },
            "ct": {
                "role_name": "Community Team",
                "category_id": 1385364624337141973,
                "role_id": 1385365339264516177
            },
            "mgmt": {
                "role_name": "Management Team",
                "category_id": 1385364707073986571,
                "role_id": 1385365141507408032
            }
        }

    @commands.command()
    async def transfer(self, ctx, department: str):
        """Transfers a channel to a different department category, pings the role, and sends an embed."""
        if department not in self.departments:
            await ctx.send(f"Invalid department: {department}. Available departments: {', '.join(self.departments.keys())}.")
            return

        category_id = self.departments[department]["category_id"]
        role_id = self.departments[department]["role_id"]
        role_name = self.departments[department]["role_name"]

        channel = ctx.channel
        if channel.category and channel.category.id == category_id:
            await ctx.send(f"This channel is already in the {department} department.")
            return

        category = ctx.guild.get_channel(category_id)
        if not category or not isinstance(category, discord.CategoryChannel):
            await ctx.send("Target category not found.")
            return

        await channel.edit(category=category)
        role = ctx.guild.get_role(role_id)
        reply_command = self.bot.get_command("reply")
        embed = discord.Embed(
            title="Transfer",
            description=f"You are being transferred to the {role_name}. "
                        f"Please remain patient while we find a staff member to assist you.",
        )
        reply_command = self.bot.get_command("reply")
        await ctx.send(content=role.mention)
        await ctx.invoke(reply_command, message=embed)

async def setup(bot):
    await bot.add_cog(Transfer(bot))

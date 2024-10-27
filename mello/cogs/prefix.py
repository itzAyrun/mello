from discord import Embed, app_commands
from discord.ext import commands

from mello.configloader import config
from mello.exceptions import (
    PrefixTooLong,
    PrefixAlreadyExists,
    PrefixDeletionError,
    PrefixNotFound,
)
from mello.emojis import GREEN_TICK, RED_CROSS


class Prefix(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_command_error(self, ctx: commands.Context, error: Exception) -> None:
        if isinstance(error, PrefixTooLong):
            ctx.__setattr__("_ignore_me_", True)
            await ctx.reply(
                embed=Embed(
                    description=f"{RED_CROSS} The prefix cannot be more than 2 characters long!"
                ),
                ephemeral=True,
            )

        elif isinstance(error, PrefixAlreadyExists):
            ctx.__setattr__("_ignore_me_", True)
            await ctx.reply(
                embed=Embed(
                    description=f"{RED_CROSS} The provided prefix already exists!"
                ),
                ephemeral=True,
            )

        elif isinstance(error, PrefixDeletionError):
            ctx.__setattr__("_ignore_me_", True)
            await ctx.reply(
                embed=Embed(
                    description=f"{RED_CROSS} Cannot remove the only active prefix!"
                ),
                ephemeral=True,
            )

        elif isinstance(error, PrefixNotFound):
            ctx.__setattr__("_ignore_me_", True)
            await ctx.reply(
                embed=Embed(
                    description=f"{RED_CROSS} The provided prefix doesn't exist!"
                ),
                ephemeral=True,
            )

    @commands.hybrid_group(
        name="prefix",
        description="Lists all active command prefixes",
        fallback="list",
    )
    @commands.cooldown(
        1, config.get_command("prefix")["cooldown"], commands.BucketType.user
    )
    async def prefix(self, ctx: commands.Context) -> None:
        embed_description = "Here are all the active command prefixes:\n\n"
        for prefix in config.get_prefix():
            embed_description += f"{prefix}\n"

        await ctx.reply(embed=Embed(description=embed_description), ephemeral=True)

    @prefix.command(
        name="add",
        description="Adds a new command prefix for the server",
    )
    @app_commands.describe(
        prefix="The prefix to add to the command list, e.g., '?', '!', ','"
    )
    @commands.cooldown(
        1,
        config.get_command("prefix")["cooldown"],
        commands.BucketType.user,
    )
    @commands.has_any_role(*config.get_command("prefix")["allowed_roles"])
    async def add(self, ctx: commands.Context, prefix: str) -> None:
        config.add_prefix(prefix)
        await ctx.reply(
            embed=Embed(
                description=f"{GREEN_TICK} Prefix `{prefix}` successfully added!"
            ),
            ephemeral=True,
        )

    @prefix.command(
        name="delete",
        description="Deletes an existing command prefix",
    )
    @app_commands.describe(prefix="The prefix to delete from the command list")
    @commands.cooldown(
        1,
        config.get_command("prefix")["cooldown"],
        commands.BucketType.user,
    )
    @commands.has_any_role(*config.get_command("prefix")["allowed_roles"])
    async def delete(self, ctx: commands.Context, prefix: str) -> None:
        config.delete_prefix(prefix)
        await ctx.reply(
            embed=Embed(
                description=f"{GREEN_TICK} Prefix `{prefix}` successfully removed!"
            ),
            ephemeral=True,
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Prefix(bot))

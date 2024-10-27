import asyncio
import argparse
import os
import logging
import logging.handlers
from typing import List

import discord
from discord import Embed
from discord.ext import commands
from dotenv import load_dotenv

from mello.emojis import RED_CROSS
from mello.configloader import config

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--test", action="store_true")
args = parser.parse_args()


class Mello(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=self.determine_prefix,
            intents=discord.Intents.all(),
            help_command=None,
            case_insensitive=True,
        )

    @staticmethod
    def determine_prefix(bot: commands.Bot, message: discord.Message) -> List[str]:
        prefixes = config.get_prefix()
        return commands.when_mentioned_or(*prefixes)(bot, message)

    async def load_cogs(self) -> None:
        for file in os.listdir("mello/cogs"):
            if file in ["__pycache__", "__init__.py"]:
                continue  # ignore

            else:
                await self.load_extension(f"mello.cogs.{file[:-3]}")

    async def on_command_error(
        self, ctx: commands.Context, error: commands.CommandError
    ) -> None:
        if hasattr(ctx, "_ignore_me_"):
            return

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.reply(
                embed=Embed(
                    description=f"{RED_CROSS} Slow down! This command is on cooldown. Try again in {round(error.retry_after, 1)} seconds.",
                ),
                ephemeral=True,
            )

        elif isinstance(error, commands.MissingAnyRole):
            missing_role_names = []
            for role_snowflake in error.missing_roles:
                if ctx.guild is not None:
                    if isinstance(role_snowflake, int):
                        missing_role_name = ctx.guild.get_role(role_snowflake).name  # type: ignore

                    else:
                        missing_role_name = role_snowflake

                    if missing_role_name is not None:
                        missing_role_names.append(missing_role_name)

            embed_description = (
                f"{RED_CROSS} You do not have the required roles to use this command.\n"
                "Please ensure you have one of the following roles:\n\n"
                f"`{', '.join(missing_role_names)}`"
            )

            await ctx.reply(embed=Embed(description=embed_description))

        else:
            developer_id = config.get_developer_id()
            embed_description = (
                f"{RED_CROSS} An unknown error occurred. "
                f"Please contact my developer {self.get_user(developer_id).mention} for more info!"  # type: ignore
            )
            await ctx.reply(embed=Embed(description=embed_description), ephemeral=True)

    async def setup_hook(self) -> None:
        await self.load_cogs()
        await self.tree.sync()

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}")


async def main() -> None:
    logger = logging.getLogger("discord")
    logger.setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        filename="logs/discord.log",
        encoding="utf-8",
        maxBytes=32 * 1024 * 1024,  # 32 MiB
        backupCount=5,  # Rotate through 5 files
    )

    dt_fmt = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(
        "[{asctime}] [{levelname}] {name}: {message}", dt_fmt, style="{"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    async with Mello() as bot:
        if args.test:
            await bot.start(os.getenv("TEST_TOKEN"))  # type: ignore
        else:
            await bot.start(os.getenv("BOT_TOKEN"))  # type: ignore


if __name__ == "__main__":
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print("keyboard interrupt detected. shutting down.")

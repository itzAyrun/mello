import random

from discord.ext import commands

RESPONSES = [
    "Hello! How can I assist you today?",
    "Hey there! What's up?",
    "Good to see you! How's it going?",
    "Hi! Hope you're doing well!",
    "Greetings! What can I do for you?",
    "Hello! How’s everything?",
    "Hey! What brings you here today?",
    "Hi there! Need any help?",
    "Hello! Always a pleasure!",
    "Hey, nice to see you!",
    "Hi! How’s your day so far?",
    "Greetings! How are you today?",
    "Hello! What’s new with you?",
    "Hey there! Anything on your mind?",
    "Hi! Ready to chat?",
    "Good day! How can I help?",
    "Hello there! What's going on?",
    "Hi! Let’s make today productive!",
    "Hey! How’s your day treating you?",
    "Hello! Let’s get started!",
    "Hi! Any questions for me?",
    "Hey! How’s everything going?",
    "Greetings! What’s up?",
    "Hi there! How can I assist?",
    "Hello! Anything I can do for you?",
    "Hey! How are things with you?",
    "Hello! What’s on the agenda?",
    "Hi! Ready to tackle some questions?",
    "Hey! How’s it going?",
    "Hello there! Let’s get to it!",
]


class Hello(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.hybrid_command(
        name="hello",
        description="Greets the user back with a random response!",
        aliases=["hi", "hey"],
    )
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def hello(self, ctx: commands.Context) -> None:
        await ctx.reply(random.choice(RESPONSES), ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Hello(bot))

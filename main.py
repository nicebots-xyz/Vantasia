import discord
import logging
from src.config.settings import DISCORD_TOKEN
from src.extensions import bestof

bot = discord.Bot()

logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, name="your commands"
        )
    )

@bot.event
async def on_application_command_error(ctx, error):
    await ctx.respond(
        f"An error occured: {error}, please retry (if it's a cooldown just wait)",
        ephemeral=True,
    )

bestof.load(bot)

bot.run(DISCORD_TOKEN)

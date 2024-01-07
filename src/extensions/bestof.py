import discord
import time

from discord.ext import commands

from ..models.base import init_db, AsyncSessionLocal
from ..models import Video, Channel, BestOf as BestOfModel, User
from ..chore import BestOfProcessor
from ..config.settings import TOS_HASH, TOS_URL


class BestOf(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, ctx: discord.ApplicationContext) -> None:
        """Checks that the bot is alive"""
        await ctx.respond("Pong!")

    @commands.slash_command()
    #    @commands.cooldown(1, 60*60*15, commands.BucketType.user)
    async def bestof(
        self,
        ctx: discord.ApplicationContext,
        video_url: discord.Option(str, "The video url"),
    ) -> None:
        """Creates a new bestof"""
        await ctx.respond("Loading...")
        async with AsyncSessionLocal() as session:
            user = await session.get(User, ctx.author.id)
            if user is None:
                user = User(
                    user_id=ctx.author.id,
                    join_date=int(time.time()),
                    last_used_date=int(time.time()),
                )
                session.add(user)
                await session.commit()
        if user.tos_hash_accepted != TOS_HASH:
            # user must click on a button to accept the TOS
            view = discord.ui.View()
            button = discord.ui.Button(
                label="I accept the TOS",
                style=discord.ButtonStyle.green,
                custom_id="accept_tos",
            )

            # add a callback to the button
            async def callback(interaction: discord.Interaction):
                await interaction.response.defer()
                async with AsyncSessionLocal() as session:
                    user = await session.get(User, ctx.author.id)
                    user.tos_hash_accepted = TOS_HASH
                    await session.commit()
                await interaction.message.edit(view=None)
                bestof_processor = BestOfProcessor(video_url, ctx)
                await bestof_processor.start()

            button.callback = callback
            view.add_item(button)
            await ctx.edit(
                content=f"Please accept the TOS found at {TOS_URL} before using the bot",
                view=view,
            )
        else:
            bestof_processor = BestOfProcessor(video_url, ctx)
            await bestof_processor.start()

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """Prints the bot's username and ID when it is ready"""
        print(f"Logged in as {self.bot.user} ({self.bot.user.id})")
        await init_db()


def load(bot: discord.Bot) -> None:
    """Loads the bestof extension"""
    bot.add_cog(BestOf(bot))


def unload(bot: discord.Bot) -> None:
    """Unloads the bestof extension"""
    bot.remove_cog("BestOf")

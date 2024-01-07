import discord
import time
import os
import pytube
import asyncio
import orjson
import io

from ..models.base import AsyncSessionLocal
from ..models import Video, Channel, BestOf as BestOfModel, User
from ..downloaders import download_youtube_audio
from ..processors import getBestofs, getTranscript, createTimeline, getBestOfsOAI
from ..config.settings import DOWNLOAD_PATH, TOS_URL
from ..utils.formatTranscript import formatTranscript


class FramerateModal(discord.ui.Modal):  # Modal to ask for framerate
    def __init__(self, user_id: int, *args, **kwargs):
        super().__init__(title="Specify framerate", *args, **kwargs)
        self.add_item(
            discord.ui.InputText(
                label="Your video's framerate (default: 29.97)",
                placeholder="29.97",
                min_length=1,
                max_length=5,
            )
        )
        self.user_id = user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            return await interaction.response.send_message(
                "You do not have the permission to do this!", ephemeral=True
            )
        await interaction.response.send_message("Frame rate set!", ephemeral=True)

    def get_value(self):
        return self.children[0].value


class FramerateSelect(discord.ui.Select):
    def __init__(
        self, processor: "BestOfProcessor", user_id: int, bestof_id, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.add_option(label="29.97", description="29.97", value="29.97")
        self.add_option(label="30", description="30", value="30")
        self.add_option(label="60", description="60", value="60")
        self.add_option(label="custom", description="custom", value="custom")
        self.processor = processor
        self.user_id = user_id
        self.bestof_id = bestof_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            return await interaction.response.send_message(
                "You do not have the permission to do this!", ephemeral=True
            )
        if interaction.data["values"][0] == "custom":
            modal = FramerateModal(self.user_id)
            await interaction.response.send_modal(modal)
            await modal.wait()
            value = modal.get_value()
        else:
            value = interaction.data["values"][0]

        frame_rate = float(value)
        async with AsyncSessionLocal() as session:
            bestof: BestOfModel = await session.get(BestOfModel, int(self.bestof_id))
            await session.refresh(bestof, ["BESTOF_INDEXES"])
            json_timeline = createTimeline(
                bestof.BESTOF_INDEXES, self.processor.video.transcript, frame_rate
            )
            json_loaded = orjson.loads(json_timeline)
            jsonfile = io.BytesIO(json_timeline.encode("utf-8"))
            await interaction.respond(
                content="Here is your otio file!",
                file=discord.File(
                    jsonfile, filename=f"{bestof.title.replace(' ', '_')}.otio"
                ),
                ephemeral=True,
            )


class AcceptButton(discord.ui.Button):  # Accept button for the TOS
    def __init__(self, label, style, custom_id, processor, user_id: int):
        super().__init__(label=label, style=style, custom_id=custom_id)
        self.processor = processor
        self.user_id = user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            return await interaction.response.send_message(
                "You do not have the permission to do this!", ephemeral=True
            )
        await interaction.response.defer()
        await interaction.message.edit(view=None)
        await self.processor.process()


class ContinueButton(
    discord.ui.Button
):  # Continue making bestofs evev if some already exist
    def __init__(
        self, label, style, custom_id, processor: "BestOfProcessor", user_id: int
    ):
        super().__init__(label=label, style=style, custom_id=custom_id)
        self.processor = processor
        self.user_id = user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            return await interaction.response.send_message(
                "You do not have the permission to do this!", ephemeral=True
            )
        await interaction.response.defer()
        await interaction.message.edit(view=None)
        await self.processor.makeBestOfs()
        await self.processor.final()


class SkipButton(discord.ui.Button):  # Skip making bestofs when some already exist
    def __init__(self, label, style, custom_id, processor, user_id: int):
        super().__init__(label=label, style=style, custom_id=custom_id)
        self.processor = processor
        self.user_id = user_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.user_id:
            return await interaction.response.send_message(
                "You do not have the permission to do this!", ephemeral=True
            )
        await interaction.response.defer()
        await interaction.message.edit(view=None)
        await self.processor.final()


class BestOfProcessor:
    """
    A class to process a video and create bestofs from its transcript.

    Attributes:
    - video_url (str): The URL of the video to process.
    - ctx (discord.ApplicationContext): The context of the command that triggered the processing.
    - user (discord.User): The user who triggered the processing.
    - user_id (int): The ID of the user who triggered the processing.
    - platform (str): The platform of the video (e.g. "youtube").
    - video_id (str): The ID of the video.
    - channel_id (str): The ID of the channel the video belongs to.
    - title (str): The title of the video.
    - thumbnail (str): The URL of the video's thumbnail.
    - full_video_id (str): The full ID of the video (e.g. "yo_video_id").
    - path (str): The path where the video is downloaded.
    - channel (Channel): The channel the video belongs to.
    - video (Video): The video object.
    """

    def __init__(self, video_url: str, ctx: discord.ApplicationContext) -> None:
        self.video_url = video_url
        self.ctx = ctx
        self.user = ctx.author
        self.user_id = ctx.author.id
        self.platform = None

    def detectPlatform(self) -> str:
        return "youtube"  # TODO: detect platform & add Twitch support

    def getVideoInfo(self) -> None:
        self.platform = self.detectPlatform()
        if self.platform == "youtube":
            video = pytube.YouTube(self.video_url)
            self.video_id = video.video_id
            self.channel_id = video.channel_id
            self.title = video.title
            self.thumbnail = video.thumbnail_url
        else:
            raise NotImplementedError("This platform is not supported yet")
        self.full_video_id = f"{self.platform[:2]}_{self.video_id}"
        self.path = os.path.join(DOWNLOAD_PATH, self.full_video_id)

    async def isUserClaimer(self) -> bool:
        async with AsyncSessionLocal() as session:
            channel: Channel = await session.get(Channel, self.channel_id)
            if channel is None:
                return False
            elif channel.claimer_id != self.user_id:
                return False
            else:
                self.channel = channel
                return True

    async def isVideoTranscripted(self) -> bool:
        # check if it is in the database, if not just false
        async with AsyncSessionLocal() as session:
            video: Video = await session.get(Video, self.full_video_id)
            if video is None:
                return False
            else:
                return True

    async def isVideoDownloaded(self) -> bool:
        # is true if any file starting with audio exists in
        if os.path.exists(self.path) and any(
            [filename.startswith("audio") for filename in os.listdir(self.path)]
        ):
            print("audio file exists")
            return True
        else:
            print("audio file does not exist")
            return False

    async def downloadVideo(self) -> None:
        match self.platform:
            case "youtube":
                await download_youtube_audio(self.video_url, self.path)
            case _:
                raise NotImplementedError("This platform is not supported yet")

    def audio_path(self) -> str:
        return [
            os.path.join(self.path, filename)
            for filename in os.listdir(self.path)
            if filename.startswith("audio")
        ][0]

    async def transcribeVideo(self) -> None:
        transcript = await getTranscript(self.audio_path())
        async with AsyncSessionLocal() as session:
            video = Video(
                video_id=self.full_video_id,
                platform=self.platform,
                url=self.video_url,
                create_date=int(time.time()),
                transcript=transcript,
            )
            session.add(video)
            await session.commit()

    async def makeBestOfs(self) -> None:
        async with AsyncSessionLocal() as session:
            video: Video = await session.get(Video, self.full_video_id)
            await session.refresh(video, ["transcript"])
        bestofs = await getBestOfsOAI(formatTranscript(video.transcript))
        #        bestofs = await getBestOfsOAI(formatTranscript(video.transcript))
        async with AsyncSessionLocal() as session:
            for bestof in bestofs:
                bestofobj = BestOfModel(
                    title=bestof["title"],
                    video_id=self.full_video_id,
                    create_date=int(time.time()),
                    JSON_OTL={},
                    BESTOF_INDEXES=bestof["parts"],
                    creator_id=self.user_id,
                )
                session.add(bestofobj)
                await session.commit()

    async def start(self) -> None:
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self.getVideoInfo)
        button = AcceptButton(
            "I accept the above mentioned",
            discord.ButtonStyle.green,
            "accept_everytime",
            self,
            self.user_id,
        )
        view = discord.ui.View()
        view.add_item(button)
        await self.ctx.edit(
            content=f"By clicking on the button below, you confirm that you have the necessary rights to use the video and give the bot express authorization to download the video's audio and process it through multiple AI algorithms as described in the Terms of Service ({TOS_URL}).",
            view=view,
        )

    async def hasBestOfs(self) -> bool:
        async with AsyncSessionLocal() as session:
            video: Video = await session.get(Video, self.full_video_id)
            await session.refresh(video, ["bestofs"])
            bestofs = [
                bestof for bestof in video.bestofs if bestof.creator_id == self.user_id
            ]
            if len(bestofs) == 0:
                return False
            else:
                return True

    async def process(self) -> None:
        await self.ctx.edit(content="Processing...")
        if not await self.isVideoTranscripted():
            if not await self.isVideoDownloaded():
                await self.ctx.edit(content="Downloading audio...")
                await self.downloadVideo()
            await self.ctx.edit(content="Transcribing audio...")
            await self.transcribeVideo()
        await self.ctx.edit(content="Making bestofs...")
        if await self.hasBestOfs():
            view = discord.ui.View()
            continue_button = ContinueButton(
                "Continue", discord.ButtonStyle.green, "continue", self, self.user_id
            )
            skip_button = SkipButton(
                "Skip", discord.ButtonStyle.red, "skip", self, self.user_id
            )
            view.add_item(continue_button)
            view.add_item(skip_button)
            await self.ctx.edit(
                content="Bestofs already exist for this video. Do you want to continue making bestofs or skip?",
                view=view,
            )
        else:
            await self.makeBestOfs()
            await self.final()

    async def final(self):
        embed = discord.Embed(
            description=f"""# Bestofs created for [`{self.title}`]({self.video_url})!
## Below is the procedure to import the bestofs into Davinci Resolve:
0. Download the otio file generated by this bot by selecting it in the dropdown below
1. Create a new project in Davinci Resolve
2. Create a new blank folder
3. Download the video from youtube in that folder. **Rename the video to video.mp4**
4. Select a video below, select a framerate and download the otio file that will be sent in that folder too
6. At the top left, click on file -> import -> timeline and import thr otio file generated by this bot in the folder
7. You should be done, that's it!**
""",
            color=discord.Color.brand_green(),
            image=self.thumbnail,
        )
        view = discord.ui.View()
        async with AsyncSessionLocal() as session:
            video: Video = await session.get(Video, self.full_video_id)
            await session.refresh(video, ["bestofs", "transcript"])
            bestofs: list[BestOfModel] = video.bestofs
            # we only want the ones with the user as creator
            bestofs = [
                bestof for bestof in bestofs if bestof.creator_id == self.user_id
            ]
            dropdown = discord.ui.Select(
                placeholder="Select a BestOf",
                min_values=1,
                max_values=1,
                options=[
                    discord.SelectOption(
                        label=str(bestof.title), value=str(bestof.bestof_id)
                    )
                    for bestof in bestofs
                ],
            )
        await self.ctx.edit(content="", embed=embed, view=view)
        self.video = video

        async def callback(interaction: discord.Interaction):
            print("callback of dropdown\n\n\n")
            if interaction.user.id != self.user_id:
                return await interaction.response.send_message(
                    "You are not the creator of this bestof!", ephemeral=True
                )
            await interaction.response.defer()
            framerateselect = FramerateSelect(
                self, self.user_id, interaction.data["values"][0]
            )
            view = discord.ui.View()
            view.add_item(framerateselect)
            await interaction.respond(
                content="Please select the framerate of your bestof",
                view=view,
                ephemeral=True,
            )

        dropdown.callback = callback
        view.add_item(dropdown)
        await self.ctx.edit(content="", embed=embed, view=view)
import pytube
import asyncio
import os
from ..config.settings import DOWNLOAD_PATH


async def donwload_audio(url: str, download_dir) -> tuple[str, str, str]:
    """
    Downloads a YouTube video from the given URL and saves it to disk.

    Args:
        url (str): The URL of the YouTube video to download.

    Returns:
        Tuple[str, str, str]: A tuple containing the path to the downloaded video directory, the title of the video, and the video ID.
    """
    video = pytube.YouTube(url)
    video_dir = download_dir
    if os.path.exists(video_dir):
        return video_dir, video.title
    os.makedirs(video_dir, exist_ok=True)
    # run in executor
    audio = video.streams.filter(only_audio=True).order_by("abr").desc().first()
    audio_path = await asyncio.get_event_loop().run_in_executor(
        None, audio.download, video_dir
    )
    extension = os.path.splitext(audio_path)[1]
    new_audio_path = os.path.join(video_dir, "audio" + extension)
    os.rename(audio_path, new_audio_path)
    return video_dir

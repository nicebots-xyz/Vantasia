from ..config.settings import openaiClient


async def getTranscript(audio_path: str):
    """
    Transcribes the audio file at the given path using the OpenAI Whisper model.

    Args:
        audio_path (str): The path to the audio file to transcribe.

    Returns:
        dict: A dictionary containing the transcribed text and other metadata.
    """
    response: dict = await openaiClient.audio.transcriptions.create(
        response_format="verbose_json",
        model="whisper-1",
        file=open(audio_path, "rb"),
    )
    return response

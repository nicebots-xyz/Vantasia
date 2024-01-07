def formatTranscript(raw: dict) -> dict:
    """Format the transcript to be more readable."""
    return {str(i): raw["segments"][i]["text"] for i in range(len(raw["segments"]))}

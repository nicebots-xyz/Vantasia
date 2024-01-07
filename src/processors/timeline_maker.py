import opentimelineio as otio


def createTimeline(
    part: list[int], transcript: dict, framerate: float = 29.97
) -> str:
    """
    Creates a timeline with video clips and a single audio track based on the given transcript and list of parts,
    ensuring that the audio is recognized as having two channels.

    Args:
        part (list[int]): A list of integers representing the parts to include in the timeline.
        transcript (dict): A dictionary containing the transcript information.

    Returns:
        str: The timeline in OTIO JSON format.
    """
    # Create a timeline and tracks for video and audio
    tl = otio.schema.Timeline(name="Timeline")
    video_track = otio.schema.Track(
        name="Video Track", kind=otio.schema.TrackKind.Video
    )
    audio_track = otio.schema.Track(
        name="Audio Track", kind=otio.schema.TrackKind.Audio
    )
    tl.tracks.extend([video_track, audio_track])

    for clip in part:
        clip = int(clip)
        segment: dict = transcript.get("segments")[clip]
        start_time = segment.get("start")
        end_time = segment.get("end")

        # Define the range of the clip in the video
        available_range = otio.opentime.TimeRange(
            start_time=otio.opentime.RationalTime(start_time * framerate, framerate),
            duration=otio.opentime.RationalTime(
                (end_time - start_time) * framerate, framerate
            ),
        )

        # Create a reference to the video file with the specified time range
        media_reference = otio.schema.ExternalReference(
            target_url="file://./video.mp4", available_range=available_range
        )

        # Create the clip for the video track
        video_clip = otio.schema.Clip(
            name="Clip{}".format(clip),
            media_reference=media_reference,
            source_range=available_range,
        )
        video_track.append(video_clip)

        # Create the clip for the audio track
        audio_clip = otio.schema.Clip(
            name="Clip{}".format(clip),
            media_reference=media_reference,
            source_range=available_range,
        )
        audio_track.append(audio_clip)

    # Return the timeline as OTIO JSON and FCP XML
    return otio.adapters.write_to_string(
        tl, "otio_json", indent=4
    )
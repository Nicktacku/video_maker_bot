import os
import random
from moviepy.editor import (
    VideoFileClip,
    CompositeVideoClip,
    ImageClip,
    AudioFileClip,
    CompositeAudioClip,
    concatenate_videoclips,
    concatenate_audioclips,
)
from PIL import Image

# todo: make resize height? use text maybe instead of image?


def create_video(lengths, r_id, title):
    try:
        os.makedirs(f"exports/{r_id}")
    except FileExistsError:
        pass

    total_length = sum(lengths) + 1
    starting_duration = random.randint(0, 4770 - int(total_length))
    clip = VideoFileClip("bg.mp4").subclip(
        starting_duration, starting_duration + int(total_length)
    )

    screenshots = []
    for ctr, image in enumerate(os.listdir(f"screenshots/{r_id}")):
        print("duration:", lengths[ctr])
        screenshot = f"screenshots/{r_id}/{ctr}.png"
        screenshots.append(
            ImageClip(screenshot)
            .set_duration(lengths[ctr])
            .margin(left=40, top=700, opacity=0)
        )

    compiled = concatenate_videoclips(screenshots, method="compose")

    tts = []
    for ctr, audio in enumerate(os.listdir(f"speeches/{r_id}")):
        print(audio)
        ctr += 1
        print(ctr)
        if lengths[ctr-1] > 0:
            tts.append(AudioFileClip(f"speeches/{r_id}/{ctr}.wav"))

    final_audio = concatenate_audioclips(tts)
    print()
    print(final_audio)

    clip.audio = final_audio

    final = CompositeVideoClip([clip, compiled])

    try:
        final.write_videofile(f"exports/{r_id}/{title}.mp4")
    except Exception:
        print(Exception)


# .margin(left=350, top=500, opacity=0)

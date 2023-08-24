import mutagen
from mutagen.wave import WAVE
import pyttsx3
import os


def create(title, stories, r_id):
    lengths = []
    ctr = 0
    try:
        os.makedirs(f"speeches/{r_id}")
    except FileExistsError:
        pass
    engine = pyttsx3.init()
    engine.save_to_file(title, f"speeches/{r_id}/{ctr+1}.wav")
    engine.runAndWait()

    audio = WAVE(f"speeches/{r_id}/{ctr+1}.wav")
    lengths.append(audio.info.length)
    for story in stories:
        ctr += 1
        text = story
        engine = pyttsx3.init()
        engine.save_to_file(text, f"speeches/{r_id}/{ctr+1}.wav")
        engine.runAndWait()

        audio = WAVE(f"speeches/{r_id}/{ctr+1}.wav")
        lengths.append(audio.info.length)

    return lengths

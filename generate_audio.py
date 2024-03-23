from gtts import gTTS
from pydub import AudioSegment
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TRCK, ID3NoHeaderError
from mutagen.mp3 import MP3
import os
import shutil

from data import (sentences, czech_sentences, LESSON, TARGET_LANGUAGE,
                  DESITNATION_DIR, DECK_NAME)
from create_deck import create_deck


def add_metadata(file_path, artist, album, title, composition_number):
    audio = MP3(file_path, ID3=ID3)
    if audio.tags is None:  # Check if the file has ID3 tag, if not, initialize it
        audio.add_tags()

    audio.tags.add(TPE1(encoding=3, text=artist))
    audio.tags.add(TALB(encoding=3, text=album))
    audio.tags.add(TIT2(encoding=3, text=title))
    audio.tags.add(TRCK(encoding=3, text=str(composition_number)))

    audio.save()


def main():
    # Ensure the output directory exists
    output_dir = f'{TARGET_LANGUAGE.lower()}_{LESSON}'
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(DESITNATION_DIR, exist_ok=True)

    cz_paths = []

    for i, (english_sentence, czech_sentence) in enumerate(zip(sentences, czech_sentences), start=1):
        # Generate English audio
        tts_en = gTTS(text=english_sentence, lang='en')
        en_path = f"{output_dir}/en_{i}.mp3"
        tts_en.save(en_path)

        # Generate Czech audio and concatenate with 2 seconds of silence in between
        combined_cz = AudioSegment.silent(duration=2000)  # Start with 2 seconds of silence

        # prepare Czech phrase
        tts_cz = gTTS(text=czech_sentence, lang='cs')
        cz_path = f"cz_{i}.mp3"

        tts_cz.save(cz_path)
        cz_paths.append(cz_path)
        add_metadata(cz_path, "Auto Czech (only Czech)", f"Auto Czech {LESSON}", czech_sentence, composition_number=i)

        cz_audio = AudioSegment.from_mp3(cz_path)

        for _ in range(3):
            combined_cz += cz_audio + AudioSegment.silent(duration=2000)
        
        # Combine English and Czech audio with 2 seconds of silence in between
        en_audio = AudioSegment.from_mp3(en_path)
        final_audio = en_audio + combined_cz

        # Save the final audio file
        final_path = f"{output_dir}/auto_cz_{i}.mp3"
        final_audio.export(final_path, format="mp3")

        # Add metadata with mutagen
        add_metadata(final_path, "Auto Czech", f"Auto Czech {LESSON}", czech_sentence, composition_number=i)

        # Clean up temporary files
        os.remove(en_path)

    create_deck()

    for cz_path in cz_paths:
        os.remove(cz_path)

    print("Audio generation complete.")

    shutil.copytree(output_dir, DESITNATION_DIR)
    shutil.copy(DECK_NAME, DESITNATION_DIR)


if __name__ == "__main__":
    main()

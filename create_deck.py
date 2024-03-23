import genanki
import random

from data import sentences, czech_sentences, LESSON, DECK_ID, MODEL_ID


# Function to generate a unique ID for the deck and model
def generate_id():
    return random.randrange(1 << 30, 1 << 31)


# Define the Anki model
my_model = genanki.Model(
    MODEL_ID,
    'Simple Model with Audio',
    fields=[
        {'name': 'English'},
        {'name': 'Czech'},
        {'name': 'Audio'},
    ],
    templates=[
        {
          'name': 'Card 1',
          'qfmt': '{{English}}<br>{{Audio}}',  # Question format
          'afmt': '{{FrontSide}}<hr id="answer">{{Czech}}',  # Answer format
        },
    ])

def create_deck():
    my_deck = genanki.Deck(DECK_ID, f'Auto Czech::Lesson {LESSON}')

    # Path to your audio files (adjust as necessary)
    media_files = []

    for i, (english, czech) in enumerate(zip(sentences, czech_sentences), start=1):
        audio_filename = f'cz_{i}.mp3'
        media_files.append(audio_filename)
        note = genanki.Note(
            model=my_model,
            fields=[english, czech, f'[sound:{audio_filename}]'])
        my_deck.add_note(note)

    # Create the package
    my_package = genanki.Package(my_deck)
    my_package.media_files = media_files

    # Export the package to an .apkg file
    output_filename = f"Auto_Czech_{LESSON}.apkg"
    my_package.write_to_file(output_filename)

    print(f"Deck '{output_filename}' has been created.")

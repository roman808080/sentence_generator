from extract_words import get_examples

LESSON = 13

MODEL_ID = 1617703258
DECK_ID = 1899843332

SOURCE_LANGUAGE = 'English'
TARGET_LANGUAGE = 'Czech'

DESITNATION_DIR = f'/Users/roman/Synchronisation/languages/{TARGET_LANGUAGE}/automatic_{TARGET_LANGUAGE.lower()}/'
DECK_NAME = f"Auto_{TARGET_LANGUAGE}_{LESSON}.apkg"

sentences = get_examples(f'{SOURCE_LANGUAGE.lower()}_{LESSON}.txt')
czech_sentences = get_examples(f'{TARGET_LANGUAGE.lower()}_{LESSON}.txt')

# Generate examples for the words that I will provide you below in the next format <word> - "<Example>". Words:


# Translate them to English in the format <word> - "<Example>".
# Patrick 25.11.2025.

from fileinput import filename
from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry the file {path} does not exist.")
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'jargon.txt', 'delightspeech.txt']

for filename in filenames:
    path = Path(filename)
    count_words(path)
# Patrick 27.11.2025.
# 10-10 Common Words.

from pathlib import Path

filenames = ['jargon.txt', 'delightspeech.txt']
user_word = input("Enter a word: ").lower()
word = f"{user_word} "

for filename in filenames:
    path = Path(filename)
    contents = path.read_text(encoding='utf-8')
    num_words = contents.lower().count(word)

    print(f"'{user_word}' appears {num_words} times in {filename}")
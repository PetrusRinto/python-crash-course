# Patrick 27.11.2025.
# 10-9 Silent Cats and Dogs.

from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(filename)

    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        print(contents)
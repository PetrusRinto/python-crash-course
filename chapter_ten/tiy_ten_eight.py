# Patrick 26.11.2025.
# 10-8 Cats and Dogs.

from pathlib import Path
from sys import path_hooks

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(filename)

    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"\nThe file {path} does not exist!\n")
    else:
        print(contents)
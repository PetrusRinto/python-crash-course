# Patrick 25.11.2025.
# FileNotFoundError Exception.

from pathlib import Path

path = Path('alice.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
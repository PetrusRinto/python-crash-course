# Patrick 24.11.2025.
# 10-2 Learning C.

from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

print(contents)

print(contents.replace('python', 'C'))
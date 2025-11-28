# Patrick 28.11.2025.
# Reading files from a json.

from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)
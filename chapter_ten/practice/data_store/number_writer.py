# Patrick 28.11.2025.
# Storing numbers into a json file.

from pathlib import Path
import json

numbers = [1, 3, 5, 7, 9, 11, 13]

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)
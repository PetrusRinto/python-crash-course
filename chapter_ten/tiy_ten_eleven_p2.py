# Patrick 28.11.2025.
# 10-11 Favorite Number.

from pathlib import Path
import json

path = Path('favorite_number.json')
contents = path.read_text()
numbers = json.loads(contents)

print(f"I know your favorite number! It's {numbers}")
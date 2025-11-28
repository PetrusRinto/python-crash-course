# Patrick 28.11.2025.
# 10-11 Favorite Number.

from pathlib import Path
import json

favorite_number = input("What is your favorite number? ")

path = Path('favorite_number.json')
contents = json.dumps(favorite_number)
path.write_text(contents)
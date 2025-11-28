# Patrick 28.11.2025.
# 10-12 Favorite Number Remembered.

from pathlib import Path
import json

def favorite_number():
    """Register the user's favorite and prints it."""
    path = Path('favorite_number.json')
    if path.exists():
        contents = path.read_text()
        number = json.loads(contents)
        print(f"I remember your favorite number! It's {number}.")
    else:
        number = input("What is your favorite number? ")
        contents = json.dumps(number)
        path.write_text(contents)

favorite_number()
        

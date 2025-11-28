# Patrick 28.11.2025.
# Saving user-generated data.

from pathlib import Path
import json

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username.title()}!")
    else:
        username = input('What is your name? ').lower()
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username.title()}!")

greet_user()
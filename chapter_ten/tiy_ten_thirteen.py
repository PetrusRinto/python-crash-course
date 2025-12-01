# Patrick 28.11.2025.
# 10-13 User Dictionary.

from pathlib import Path
import json

def get_stored_data(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        data = json.loads(contents)
        return data
    else:
        return None
    
def get_new_data(path):
    """Prompt for new data."""
    username = input('What is your name? ').lower()
    profession = input('What is your profession? ').lower()
    age = input('What is your age? ')

    data = {
        'username': f'{username}',
        'profession': f'{profession}',
        'age': f'{age}'
        }

    contents = json.dumps(data)
    path.write_text(contents)
    return data

def greet_user():
    """Greet the user by name."""
    path = Path('data.json')
    data = get_stored_data(path)
    if data:
        print(f"Welcome back, {data['username'].title()}!")
        print('\nThis is our saved data about you:')
        print(f'Username: {data['username'].title()}')
        print(f'Profession: {data['profession'].title()}')
        print(f'Age: {data['age']}')
    else:
        data = get_new_data(path)
        print(f"We'll remember you when you come back, {data['username'].title()}!")

greet_user()
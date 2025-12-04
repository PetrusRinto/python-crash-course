# Patrick 01.12.2025.
# 10-14 Verify User.

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
    goal = input('What is your life goal? ')

    data = {
        'username': username,
        'profession': profession,
        'age': age,
        'goal': goal
        }

    contents = json.dumps(data)
    path.write_text(contents)
    return data

def greet_user():
    """Greet the user by name."""
    path = Path('data.json')
    data = get_stored_data(path)
    
    if data:

        verify = input(f'Is {data['username'].title()} your name? (y/n) ')

        if verify == 'y':
            print(f"Welcome back, {data['username'].title()}!")
            print('\nThis is our saved data about you:')
            print(f'Username: {data['username'].title()}')
            print(f'Profession: {data['profession'].title()}')
            print(f'Age: {data['age']}')
            print(f'Goal: {data['goal']}')
        else:
            data = get_new_data(path)
            print(f"We'll remember you when you come back, "
                f"{data['username'].title()}!")

    else:
        data = get_new_data(path)
        print(f"We'll remember you when you come back, "
              f"{data['username'].title()}!")

greet_user()
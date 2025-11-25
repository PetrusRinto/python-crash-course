# Patrick 25.11.2025.
# 10-5 Guest Book.

from pathlib import Path
    
print("Exit anytime with 'q'!")
contents = ''

active = True

while active:

    guest_name = input('\nWhat is your name? ')
    contents += f"{guest_name}\n"

    question = input('Continue? y/n ')
    if question == 'y':
        continue
    else:
        active = False

path = Path('guest_book.txt')
path.write_text(contents)
    
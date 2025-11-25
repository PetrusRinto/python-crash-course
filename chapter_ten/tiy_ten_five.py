# Patrick 25.11.2025.
# 10-5 Guest Book.

from pathlib import Path
    
print("Exit anytime with 'q'!")
contents = ''

active = True

while active:

    guest_name = input('\nWhat is your name? ')
    if guest_name == 'q':
        active = False
        continue
    else:
        contents += f"{guest_name}\n"

path = Path('guest_book.txt')
path.write_text(contents)
    
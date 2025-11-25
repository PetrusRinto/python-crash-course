# Patrick 25.11.2025.
# 10-4 Guest.

from pathlib import Path


guest_name = input("What is your name? ")

path = Path('guest.txt')
path.write_text(guest_name)
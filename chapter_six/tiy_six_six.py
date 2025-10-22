# Patrick 22.10.2025.
# 6-6 Polling.

# Dictionary from page 96 in "Python Crash Course, 3rd Edtion".
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

# List of recommended poll takers.
poll_takers = ['jen', 'sarah', 'edward', 'margaret', 'lovelace', 'alan']

# Looping through the list
for poll_taker in poll_takers:
    if poll_taker in favorite_languages:
        print(f"Thank you for responding {poll_taker.title()}!\n")
    else:
        print(f"\nHello {poll_taker.title()}, take the language poll!")
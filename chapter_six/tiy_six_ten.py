# Patrick 28.10.2025.
# 6-10 Favorite Numbers.
# Modified program from 6-2.

# Dictonary.
favorite_numbers = {
    'bjørn': [2, 7, 9],
    'natalie': [87, 27, 12],
    'patrick': [6, 12, 22],
    'oliver': [67, 41, 17],
    'nicolay': [11, 10, 8],
    }

# Looping through the dictionary.
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers:")
    print(f"\t{numbers}")
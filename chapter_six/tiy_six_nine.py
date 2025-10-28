# Patrick 27.10.2025.
# 6-9 Favorite Places.

# Dictionaries of people's favorite places.
favorite_places = {
    'rebekka': 'aquarium',
    'simon': ['japan', 'greece', 'france'],
    'maria': ['japan', 'spain', 'south korea']
    }

# Looping through the dictionary.
for name, places in favorite_places.items():
    if name == 'rebekka':
        print(f"\n{name.title()}'s favorite place needs an {places}!")
    else:
        print(f"\n{name.title()}'s favorite places are:")
        for place in places:
            print(f"\t{place.title()}.")
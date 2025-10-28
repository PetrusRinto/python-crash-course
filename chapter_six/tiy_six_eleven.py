# Patrick 28.10.2025.
# 6-11 Cities.

# Dictionary of cities.
cities = {
    'tokyo': {
        'country': 'japan',
        'population': 37000000,
        'fact': 'Tokyo backwards is Kyoto in japanese',
        },

    'berlin': {
        'country': 'germany',
        'population': 3700000,
        'fact': 'Berlin was the capital of Prussia from 1701-1871',
        },

    'steinkjer': {
        'country': 'norway',
        'population': 13060,
        'fact': 'Small town in Norway, where I had my first apprenticeship',
        },
    }

# Loop.
for city, city_info in cities.items():
    print(f"\n{city.title()}")
    print(f"\t{city_info['country']}")
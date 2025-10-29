# Patrick 29.10.2025.
# 6-11 Cities. / 6-12 Extensions.

# Dictionary of cities.
cities = {
    'tokyo': {
        'country': 'japan',
        'population': 37_000_000,
        'fact': 'Tokyo backwards is Kyoto in japanese',
        },

    'berlin': {
        'country': 'germany',
        'population': 3_700_000,
        'fact': 'Berlin was the capital of Prussia between 1701-1871',
        },

    'steinkjer': {
        'country': 'norway',
        'population': 13_060,
        'fact': 'Small town in Norway where I had my first apprenticeship',
        },
    }

# Loop.
for city, info in cities.items():
    population = info['population']
    
    # Fewer lines of if/elif statements.
    if population >= 1_000_000:
        population = f"{population // 1_000_000} million"
    elif population >= 1_000:
        population = f"{population // 1_000} thousand"

    # Cleaner output.
    print(f"\n{city.title()}:")
    print(f"\t- {city.title()} is in {info['country'].title()}.")
    print(f"\t- Its population is approximately {population}.")
    print(f"\t- Random fact: {info['fact']}.")

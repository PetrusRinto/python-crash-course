# Patrick 29.10.2025.
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
        'fact': 'Berlin was the capital of Prussia between 1701-1871',
        },

    'steinkjer': {
        'country': 'norway',
        'population': 13060,
        'fact': 'Small town in Norway, where I had my first apprenticeship',
        },
    }

# Loop.
for city, city_info in cities.items():
    city_name = city
    country = city_info['country']
    population = city_info['population']
    population = str(population)
    fact = city_info['fact']
    
# If statements for output format.
    if len(population) > 7:
        population = f"{population[:2]} million"
    elif len(population) > 6:
        population = f"{population[:1]}.{str(population)[1]} million"
    elif len(population) == 6:
        population = f"{population[:3]} thousand"
    elif len(population) > 4:
        population = f"{population[:2]} {population[2:]}"
    elif len(population) <= 4:
        population = population
# I will revisit and clean up this mess, I have an idea.
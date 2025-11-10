# Patrick 10.11.2025.
# 8-5 Cities.

def describe_city(city_name, city_country='Japan'):
    """Simple ciry description."""
    print(f"\n{city_name.title()} is in {city_country.title()}.")

# Default argument.
describe_city(city_name='tokyo')

# Default argument.
describe_city(city_name='kyoto')

# Custom argument.
describe_city(city_name='steinkjer', city_country='norway')
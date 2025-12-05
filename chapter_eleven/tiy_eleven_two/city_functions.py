# Patrick 05.12.2025.
# 11-2 Population.

def get_city_country(city, country, population=''):
    """A function that returns a city and a country."""
    city = city.lower().title()
    country = country.lower().title()
    if population:
        city_country = f"{city}, {country} - population {population}"
    else:
        city_country = f"{city}, {country}"
    return city_country
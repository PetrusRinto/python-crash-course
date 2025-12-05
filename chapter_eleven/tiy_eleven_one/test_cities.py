# Patrick 04.12.2025.
# 11-1 City, Country.

from city_functions import get_city_country

def test_city_country():
    """Testing if 'Oslo, Norway' works."""
    city_country = get_city_country('oslo', 'norway')
    assert city_country == 'Oslo, Norway'
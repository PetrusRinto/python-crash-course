# Patrick 05.12.2025.
# 11-2 Population.

from city_functions import get_city_country

def test_city_country():
    """Testing if 'Oslo, Norway' works."""
    city_country = get_city_country('oslo', 'norway')
    assert city_country == 'Oslo, Norway'

def test_city_country_population():
    """Testing if 'Oslo, Norway - population xxx' works."""
    city_country = get_city_country('oslo', 'norway', population=1100000)
    assert city_country == 'Oslo, Norway - population 1100000'
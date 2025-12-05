# Patrick 05.12.2025.
# 11-2 Population.

from city_functions import get_city_country

def test_city_country():
    """Testing if 'Oslo, Norway' works."""
    city_country = get_city_country('oslo', 'norway', '1100000')
    assert city_country == 'Oslo, Norway - population 1100000'
# Patrick 13.11.2025.
# 9-2 Three Restaurants.

from tiy_nine_one import Restaurant

# Creating three instances from the class in 9-1.
restaurant_1 = Restaurant('Deli', 'pizza')
restaurant_2 = Restaurant('Freshly', 'greek')
restaurant_3 = Restaurant('Python Delight', 'dutch')

restaurants = [restaurant_1, restaurant_2, restaurant_3]

for restaurant in restaurants:
    restaurant.describe_restaurant()
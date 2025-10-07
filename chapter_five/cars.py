# Patrick 07.10.2025
# If statements.

# List of cars
cars = ['audi', 'bmw', 'subaru', 'toyota']

# Uppercase on 'bmw' and title case with the rest.
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
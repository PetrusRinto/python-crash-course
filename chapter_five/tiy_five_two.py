# Patrick 08.10.2025.
# More conditional tests.

# Testing for inequality
car = 'porsche'
house = 'small'
print("Is car == house? I predict False.")
print(car == house)

print("\nIs car == 'porsche'? I predict True.")
print(car == 'porsche')

# Testing with lower()
country = 'Japan'
print("\nIs country == 'Japan'? I predict False.")
print(country.lower() == 'Japan')

print("\nIs country == 'japan'? I predict True.")
print(country.lower() == 'japan')

# Numerical tests
age_1 = 18
age_2 = 23
print("\nIs 18 == 23? I predict False.")
print(age_1 == age_2)

print("\nIs 18 != 23? I predict True.")
print(age_1 != age_2)

print("\nIs 18 > 23? I predict False.")
print(age_1 > age_2)

print("\nIs 18 < 23? I predict True.")
print(age_1 < age_2)

print("\nIs 18 >= 23? I predict False.")
print(age_1 >= age_2)

print("\nIs 18 <= 23? I predict True.")
print(age_1 <= age_2)

# Test with 'and' and 'or'
age_1 = 18
age_2 = 23
print("\nIs 18 or 23 equal to or greater than 20? I predict True.")
print(age_1 >= 20 or age_2 >= 20)

print("\nIs 18 and 23 equal to or greater than 20? I predict False.")
print(age_1 >= 20 and age_2 >= 20)

# Testing if an item is in a list

# Patrick 08.10.2025.
# More conditional tests.

# Testing for inequality.
car = 'porsche'
house = 'small'
print("Is car == house? I predict False.")
print(car == house)

print("\nIs car == 'porsche'? I predict True.")
print(car == 'porsche')

# Testing with lower().
country = 'Japan'
print("\nIs country == 'Japan'? I predict False.")
print(country.lower() == 'Japan')

print("\nIs country == 'japan'? I predict True.")
print(country.lower() == 'japan')

# Numerical tests.
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

# Test with 'and' and 'or'.
age_1 = 18
age_2 = 23
print("\nIs 18 or 23 equal to or greater than 20? I predict True.")
print(age_1 >= 20 or age_2 >= 20)

print("\nIs 18 and 23 equal to or greater than 20? I predict False.")
print(age_1 >= 20 and age_2 >= 20)

# Testing if an item is in a list.
certifications = ['az-400', 'az-900', 'az-104']
if 'az-400' or 'az-104' in certifications:
    print("\nYou're qualified!")
else:
    print("\nYou are not qualified yet.")

# Testing if an item is not in the list.
if 'MS-500' not in certifications:
    print("\nYou are missing certification: 'MS-500'.")
else:
    print("\nAll certifications acquired!")

# Testing conditions without if statements.
subjects = ['math', 'science', 'physical education']
print('\nIs math in the list of subjects? I predict True.')
print('math' in subjects)

print('\nIs society in the list of subjects? I predict False.')
print('society' in subjects)
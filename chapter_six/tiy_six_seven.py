# Patrick 27.10.2025.
# 6-7 People.

# Dictionary.
mhamilton = {
    'first': 'margaret',
    'last': 'hamilton',
    'age': '89',
    'city': 'paoli'
    }

alovelace = {
    'first': 'ada',
    'last': 'lovelace',
    'age': '36',
    'city': 'london'
    }

aturing = {
    'first': 'alan',
    'last': 'turing',
    'age': '41',
    'city': 'london'
    }

# List of dictionaries.
people = [mhamilton, alovelace, aturing]

# Looping through each person.
for person in people:
    full_name = f"{person['first']} {person['last']}"
    age = person['age']
    city = person['city']

    print(f"\n{full_name.title()} is from {city.title()}"
          f"and is {age} years old.")
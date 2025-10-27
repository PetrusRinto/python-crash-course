# Patrick 27.10.2025.
# 6-8 Pets.

# Dictionaries of pets.
pet_1 = {
    'name': 'kasper',
    'animal': 'dog',
    'color': 'white',
    'size': 'small',
    'owner': 'cathrine'
    }
    
pet_2 = {
    'name': 'ellie',
    'animal': 'dog',
    'color': 'black',
    'size': 'medium',
    'owner': 'kristin'
    }
    
pet_3 = {
    'name': 'lynet',
    'animal': 'cat',
    'color': 'black',
    'size': 'small',
    'owner': 'sara'
    }

# List of pets.
pets = [pet_1, pet_2, pet_3]

# Looping through the pets.
for pet in pets:
    pet_name = pet['name']
    owner = pet['owner']

    print(f"\n{pet_name.title()}:")
    print(f"\tA {pet['color']} {pet['animal']}, "
          f"quite {pet['size']} in size.")
    print(f"\t{owner.title()} is the owner of this {pet['animal']}.")
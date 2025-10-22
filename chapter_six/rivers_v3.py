# Patrick 22.10.2025.
# 6-5 Riveers version 2.

# 3 well known rivers.
major_rivers = {
    'nile': 'egypt',
    'amazon river': 'peru',
    'mississippi river': 'united states',
    }

# Looping through the dictionary, creating a sentence for each.
for river, country in major_rivers.items():
    print(f"{country.title()}\n")
# Patrick 21.10.2025.
# 6-5 Rivers.

# 3 well known rivers.
major_rivers = {
    'nile': 'egypt',
    'amazon river': 'peru',
    'mississippi river': 'united states',
    }

# Looping through the dictionary, creating a sentence for each.
for river, country in major_rivers.items():
    print(f"The {river.title()} runs through {country.title()}\n")


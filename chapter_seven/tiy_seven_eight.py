# Patrick 30.10.2025 / 07.11.2025 / 10.11.2025.
# 7-8 Deli. / 7-9 No Pastrami.

# List of sandwiches.
sandwich_orders = [
    'tuna sandwich',
    'pastrami',
    'chicken sandwich',
    'pastrami',
    'ham sandwich',
    'pastrami',
    'avocado sandwich'
    ]

# Message from deli.
print('\nWe have ran out of pastrami.\n')

# Loop to remove pastrami.
while 'pastrami' in sandwich_orders:
    # Removing value with 'remove'.
    sandwich_orders.remove('pastrami')

# Empty list of finished sandwiches.
finished_sandwiches = []

# Looping through orders.
while sandwich_orders:
    made_sandwich = sandwich_orders.pop()

    # Print a message and append to finished sandwiches.
    print(f"I made your {made_sandwich.title()}!")
    finished_sandwiches.append(made_sandwich)

# Print message and list the finished sandwiches.
print("\nThe following sandwiches were made:")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich.title()}")
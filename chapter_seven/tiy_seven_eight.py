# Patrick 30.10.2025.
# 7-8 Deli.

# List of sandwiches.
sandwich_orders = [
    'tuna sandwich',
    'chicken sandwich',
    'ham sandwich',
    'avocado sandwich'
    ]

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
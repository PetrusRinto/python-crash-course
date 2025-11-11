# Patrick 11.11.2025.
# 8-12 Sandwiches.

def sandwiches(*sandwiches):
    """Print the list of sandwiches ordered."""
    print("\nOrdering a sandwich with the following toppings:")
    for topping in sandwiches:
        print(f"- {topping}")

sandwiches('ham')
sandwiches('chicken', 'chili mayo')
sandwiches('chicken', 'pesto', 'mozzarella', 'tomato')
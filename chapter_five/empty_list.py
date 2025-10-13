# Patrick 13.10.2025.
# Practising conditions in if statements.

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print(f"\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
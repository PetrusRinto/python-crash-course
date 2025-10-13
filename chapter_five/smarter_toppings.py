# Patrick 13.10.2025.
# Testing smarter conditional tests with if statements with two lists.

# First list.
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

# Second list.
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# If statements and conditions
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
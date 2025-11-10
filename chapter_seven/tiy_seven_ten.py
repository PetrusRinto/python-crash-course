# Patrick 10.11.2025.
# 7-10 Dream Vacation.

# Empty dictionary.
responses = {}

# An active flag for polling.
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, "
                     "whare would you go? ")
    
    # Storing the response in the dictionary.
    responses[name] = response

    # End the poll if no one else is participating.
    repeat = input("Would you let another peron participate? (yes / no) ")
    if repeat == 'no':
        polling_active = False

# Poll complete. Showing results.
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name.title()} would visit {response.title()}")
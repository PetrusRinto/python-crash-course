# Patrick 30.10.2025.
# 7-2 Restaurant Seating.

# Multiline string.
people = "\nHow many people are in your group?"
people += "\n: "

# Variable for input.
amount = input(people)

# Verifying conditions with if/else.
if int(amount) > 8:
    print(f"\nYou have to wait for a table.\n")
else:
    print("\nPerfect. You're table is ready!\n")
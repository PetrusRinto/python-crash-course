# Patrick 30.10.2025.
# 7-3 Multiples of Ten.

# Giving context for user input.
prompt = "\nGive me a number, any number"
prompt += "\nNumber: "

# Variable for input.
number = input(prompt)

# Checking conditions with if/else.
if int(number) % 10 == 0:
    print(f"\n{number} is a multiple of 10!\n")
else:
    print(f"\n{number} is not a multiple of 10!\n")
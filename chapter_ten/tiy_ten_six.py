# Patrick 26.11.2025.
# 10-6 Addition.


first_number = input("Enter a number: ")
second_number = input("Enter a second number: ")

try:
    added_number = int(first_number) + int(second_number)
except ValueError:
    print(f"A number was not registered!")
else:
    print(f"\n{first_number} + {second_number} = {added_number}")
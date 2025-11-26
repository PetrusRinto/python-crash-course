# Patrick 26.11.2025.
# 10-7 Addition Calculation.

print('This is a "addition-only" calculator. Add, add.')
print("Enter 'q' anytime you want to stop!\n")

active = True

while active:

    first_number = input("Enter a number: ")
    if first_number == 'q':
        active = False
        continue
    second_number = input("Enter a second number: ")
    if second_number == 'q':
        active = False
        continue
    else:
        try:
            added_number = int(first_number) + int(second_number)
        except ValueError:
            print(f"A number was not registered!\n")
        else:
            print(f"\n{first_number} + {second_number} = {added_number}\n")
    
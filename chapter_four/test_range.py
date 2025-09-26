# Patrick 26.09.2025
for value in range(0, 6): # This is powerful
    print(value)
print(f"\nThe 'range()' function in python ends on the second number '{value + 1}' in this case.")
print(f"This means python will stop the range when the *next* number is the last value defined in the program.")
print(f"Since the last number in our range() is '{value + 1}', it ends at '{value}'\n")

# Range work with single values
# Testing
single_num = 5
print(f'Testing single value in range():\n')
print(f"The program should start at '0' and stop at '{single_num - 1}' since the variable is '{single_num}'")
for single in range(single_num):
    print(f'{single}')
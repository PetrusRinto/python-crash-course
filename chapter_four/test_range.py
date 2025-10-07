# Patrick 26.09.2025
# Testing range()

# Explanation
print(f"\nTo output a list from '0-5' with range(). 0 is defined and then 6.")

print(f"An example with a short range:\n")
for value in range(0, 6): # This is powerful
    print(value)

print(f"\nThe range() stops right before the end value ({value + 1}) here.")
print("Python never includes that final number — it stops just before.")
print(f"So, since we defined up to {value + 1}, the loop ends at {value}.\n")

# Testing with single values
single_num = 5
print(f'Testing single value in range().')
print(f"It starts at 0 and ends at {single_num - 1}:\n")

# Looping through the range
for single in range(single_num):
    print(f'{single}')

print(f"\nThat's because our end value is {single_num} in this example.\n")
# Patrick 29.09.2025.
# 4-10 Slices.
# Using one of my earlier programs to slice items.

# Program from 4-9.
cubes = []
for cube in range(1, 11):
    cubes.append(cube**3)

# 4-10 assignment.
print(f'All of the items in the list:')
print(f'{cubes}\n')
print(f'The first three items in the list are:')
print(f'{cubes[:3]}\n')
print(f'The three items from the middle of the list are:')
print(f'{cubes[3:6]}\n')
print(f'The last three items in the list are:')
print(f'{cubes[-3:]}\n')
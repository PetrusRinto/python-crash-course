# Patrick 29.09.2025
# 4-8 Cubes
# A number raised to the third power from 1 through 10

# Using comprehension to avoid 'for loop' mess
cubes = [ value**3 for value in range(1, 11) ]
for cube in cubes:
    print(cube)
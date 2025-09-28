# Patrick 28.09.2025
# 4-4 One Million: Creating a list of numbers from one to a million.

# Comprehension method with a for loop to make the million list.
one_million = [ million for million in range(1, 1000001) ]
for num in one_million: # And a for loop to print each number in the list.
    print(num)
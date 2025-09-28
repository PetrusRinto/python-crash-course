# Patrick 28.09.2025
# 4-5 Summing a million
# Making a list from one to a million, and using min() and max()
# to start at one and end in one million.
# Also, need to use sum() function to test pythons' quickness.

# creating a list from one to one million
one_million = [ million for million in range(1, 1000001) ]
print(f'The list starts at: {min(one_million)}\nAnd ends at: {max(one_million)}') # Verify the list start at one and ends in one million

# Using sum() function to see how quickly Python can handle adding one million numbers
print(f'\nThe list added together: {sum(one_million)}')
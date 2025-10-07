# Patrick 28.09.2025
# 4-5 Summing a million
# Making a list from one to a million, and using min() and max()
# to start at one and end in one million.
# Also, need to use sum() function to test pythons' quickness.

# creating a list from one to one million
one_million = [ million for million in range(1, 1000001) ]
# Verification
print(f'The list start at: {min(one_million)}\nEnds at: {max(one_million)}') 

# Using sum() to see how quickly Python use math with a million numbers
print(f'\nThe list added together: {sum(one_million)}')
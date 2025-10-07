# Patrick 26.09.2025.
# Square numbers in a list with range and adding them to an empty list.

# List to store squares from range.
squares = []
# For loop to add the square numbers to the list.
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
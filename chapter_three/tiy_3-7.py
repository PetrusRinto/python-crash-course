# Patrick 12.09.2025
# The great 'guest list'
# With more changes, but less people

guests = ['jesus', 'ghandi', 'hawkins', 'stark', 'rudeus', 'kazuto', 'iroh', 'katara'] # Same list

# Adding a newline for aesthetics
print('\n')

# Oh no, Ghandi seems to be busy
too_busy = 'ghandi'
guests.remove(too_busy) # Removing Ghandi from the list

# Wait, I can invite someone else to take Ghandi's place!
new_guest = 'gwen' # No other than Gwen Stacy herself
guests.insert(1, new_guest) # Adding Gwen to the list

# Reusing the loop from before
for guest in guests:
    print(f"Dear {guest.title()}, I invite you to a humble dinner party. Well met!")
    # Output: The same list, but Ghandi gone and Gwen present
print('\n') # Newline

# Informing of more space
print('Good news! I found a bigger table.')

# Defineing extra guests for the bigger table
extra_guest1 = 'zuko'
extra_guest2 = 'aang'
extra_guest3 = 'asami'

guests.append(extra_guest1)
guests.append(extra_guest2)
guests.append(extra_guest3)

print('\n') # Newline

# Reusing the loop from before
for guest in guests:
    print(f"Dear {guest.title()}, I invite you to a humble dinner party. Well met!")
    # Output: The same list, but Ghandi gone and Gwen present
print('\n') # Newline

print(f"I can only invite two people for dinner. This is a result of the table not being able to arrive in time.")
print('\n') # Newline

# Patrick 17.09.2025
# Popping guests who are uninvited
popped_one = guests.pop(0)

popped_two = guests.pop(1)

popped_three = guests.pop(2)

popped_four = guests.pop(3)

popped_five = guests.pop(4)

popped_six = guests.pop(5)

popped_seven = guests.pop(-4)

popped_eight = guests.pop(-3)

popped_nine = guests.pop(-2)

# Storing the uninvited guests to a variable
popped_guests = [popped_one, popped_two, popped_three, popped_four, popped_five, popped_six, popped_seven, popped_eight, popped_nine]

# Looping the list to print an apology
for popped in popped_guests:
    print(f'I am so sorry {popped}, but we do not have the capacity and cannot invite you.')
print('\n') # Newline

# Letting the remaining guests know they are invited
for invited in guests:
    print(f'Good news {invited}! you are still invited. Congrats!')
print('\n') # Newline
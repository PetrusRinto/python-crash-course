# Patrick 11.09.2025
# The great 'guest list'
# With changes

guests = ['jesus', 'ghandi', 'hawkins', 'stark', 'rudeus', 'kazuto', 'iroh', 'katara'] # Same list

# Adding a newline for aesthetics
print('\n')

for guest in guests:
    print(f"Dear {guest.title()}, I invite you to a humble dinner party. Well met!") # Looped because I am lazy

# Oh no, Ghandi seems to be busy
too_busy = 'ghandi'
guests.remove(too_busy) # Removing Ghandi from the list

print(f'\nUnfortunately {too_busy.title()} is busy and can not attend.') # Sad message :(

# Wait, I can invite someone else to take Ghandi's place!
new_guest = 'gwen' # No other than Gwen Stacy herself
guests.append(new_guest) # Adding Gwen to the list

print('\n') # Newline

# Reusing the loop from before
for guest in guests:
    print(f"Dear {guest.title()}, I invite you to a humble dinner party. Well met!")
    # Output: The same list, but Ghandi gone and Gwen present
print('\n') # Newline

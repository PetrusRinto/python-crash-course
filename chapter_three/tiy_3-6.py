# Patrick 12.09.2025
# The great 'guest list'
# With more changes

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

extra_guests = ['']

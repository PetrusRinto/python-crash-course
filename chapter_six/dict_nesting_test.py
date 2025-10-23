# Patrick 23.10.2025.
# Generating a fleet of 30 aliens wirh range().

# Empty list for storing the aliens.
aliens = []

# 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

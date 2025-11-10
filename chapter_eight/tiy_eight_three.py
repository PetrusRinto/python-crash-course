# Patrick 10.11.2025.
# 8-3 T-Shirt.

def make_shirt(shirt_size, shirt_message):
    """Display size and message."""
    print(f"\nT-shirt size: {shirt_size}")
    print(f"T-shirt message: {shirt_message}!")

# Positional arguments.
make_shirt('Medium', 'Chit happens')

# Keyword arguments.
make_shirt(shirt_size='Large', shirt_message='Do it lady')
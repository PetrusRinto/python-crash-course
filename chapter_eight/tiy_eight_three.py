# Patrick 10.11.2025.
# 8-3 T-Shirt. / 8-4 Large Shirts

def make_shirt(shirt_size='Large', shirt_message='I love Python'):
    """Display size and message."""
    print(f"\nT-shirt size: {shirt_size}")
    print(f"T-shirt message: {shirt_message}!")

# Default arguments.
make_shirt()

# Keyword arguments.
make_shirt(shirt_size='Medium')

# Keyword arguments.
make_shirt(shirt_size='Small', shirt_message='Do it lady')
# Patrick 13.11.2025.
# 9-1 Restaurant.

class Restaurant:
    """Simple class describing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Prints the restaurant name and cuisine type."""

        print(f"The restaurant's name is {self.restaurant_name}")
        print(f"{self.restaurant_name}'s cuisine is {self.cuisine_type}")
    
    def open_restaurant(self):
        """Simulating that the restaurant is open."""
        
        print(f"{self.restaurant_name} is open!")
# Patrick 14.11.2025.
# 9-4 Number Served.

class Restaurant:
    """Simple class describing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Prints the restaurant name and cuisine type."""
        print(f"\nThe restaurant's name is {self.restaurant_name}")
        print(f"{self.restaurant_name}'s cuisine is {self.cuisine_type}")
    
    def open_restaurant(self):
        """Simulating that the restaurant is open."""  
        print(f"{self.restaurant_name} is open!")
    
    def read_number_served(self):
        """Reads the number of servings."""
        print(f"Served: {self.number_served}")
    
    def set_number_served(self, servings):
        """Sets the number of servings."""
        self.number_served = servings
    
    def increment_number_served(self, served):
        """Add the given amount of servings."""
        self.number_served += served


# Creating three instances from the class in 9-1.
restaurant = Restaurant('Python Delight', 'dutch')

restaurant.set_number_served(12)
restaurant.read_number_served()

restaurant.increment_number_served(4)
restaurant.read_number_served()
# Patrick 17.11.2025.
# 9-6 Ice Cream Stand.

# 18.11.2025.
# 9-10 Imported Restaurant.

"""A set of classes representing restaurants."""

class Restaurant:
    """Simple class describing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Prints the restaurant name and cuisine type."""
        print(f"The restaurant's name is {self.restaurant_name}.")
        print(f"{self.restaurant_name}'s cuisine is {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Simulating that the restaurant is open."""  
        print(f"{self.restaurant_name} is open!")
   

class IceCreamStand(Restaurant):
    """Represents a specific restaurant, serving ice cream."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'strawberry', 'chocolate']
    
    def read_flavors(self):
        """Simple method to display flavors."""
        for flavor in self.flavors:
            print(f"- {flavor}")
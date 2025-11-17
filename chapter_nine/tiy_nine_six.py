# Patrick 17.11.2025.
# 9-6 Ice Cream Stand.

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

ice_cream_stand = IceCreamStand('Creams & Ice', 'ice cream')
ice_cream_stand.describe_restaurant()
ice_cream_stand.read_flavors()
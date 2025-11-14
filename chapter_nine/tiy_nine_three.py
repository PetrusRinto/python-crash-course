# Patrick 13.11.2025.
# 9-3 Users.

class User:
    """Simulating details in a simple user profile."""

    def __init__(self, first_name, last_name, title, role):
        """Initializing attributes for the user profile."""
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.role = role
    
    def describe_user(self):
        """A method that summurize the user's details."""
        print(f"\n'{self.first_name}' user info:")
        print(f"\tFull name: {self.first_name} {self.last_name}")
        print(f"\tTitle: {self.title}")
        print(f"\tRole: {self.role}")
    
    def greet_user(self):
        """A method for greeting the user."""
        print(f"Greetings {self.first_name}!\n")

user_1 = User('Petrus', 'Rinto', 'Cloud Engineer', 'Global Reader')
user_2 = User('Bekkus', 'Plantus', 'Pharmacist', 'Global Healer')
user_3 = User('Bestus', 'Testus', 'Filler', 'Global Sealer')

users = [user_1, user_2, user_3]

for user in users:
    user.describe_user()
    user.greet_user()
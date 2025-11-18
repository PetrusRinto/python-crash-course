# Patrick 18.11.2025.
# 9-8 Privileges.

# 18.11.2025.
# 9-11 Imported Admin.

# 9-12 Multiple Modules.

"""A set of classes that can be used to represent a user."""

class User:
    """Simulating details in a simple user profile."""

    def __init__(self, first_name, last_name, title, role):
        """Initializing attributes for the user profile."""
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.role = role
        self.login_attempts = 0
    
    def describe_user(self):
        """A method that summurize the user's details."""
        print(f"\n'{self.first_name}' user info:")
        print(f"\tFull name: {self.first_name} {self.last_name}")
        print(f"\tTitle: {self.title}")
        print(f"\tRole: {self.role}")
    
    def read_login_attempts(self):
        """Reads the amount of login attempts."""
        print(f"\tAttempted logins: {self.login_attempts}")
    
    def greet_user(self):
        """A method for greeting the user."""
        print(f"Greetings {self.first_name}!")
    
    def increment_login_attempts(self):
        """Add the given amount to login attempts reading."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Resets the amount of login attempts."""
        self.login_attempts = 0
# Patrick 18.11.2025.
# 9-12 Multiple Modules.

"""A set of classes that represent an admin user."""

from user import User

class Privileges:
    """Simple attempt to represent privileges."""

    def __init__(self, privileges=['full control',
                                   'can read',
                                   'can edit']):
        """Initializes attributes for privileges."""
        self.privileges = privileges

    def show_privileges(self):
        """Simulates a display of privileges."""
        print(f"Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Simple attempt to represent an admin user."""

    def __init__(self, first_name, last_name, title, role):
        """Initiates attributes from the parent class."""
        super().__init__(first_name, last_name, title, role)
        self.privileges = Privileges()
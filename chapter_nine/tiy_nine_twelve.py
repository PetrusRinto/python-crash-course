# Patrick 18.11.2025.
# 9-12 Multiple Modules.

from user import User
from admin import Privileges, Admin

new_admin = Admin('Present', 'Tailor', 'Administrator', 'Global Administrator')
new_admin.privileges.show_privileges()
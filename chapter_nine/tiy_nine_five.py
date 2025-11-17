# Patrick 17.11.2025.
# 9-5 Login Attempts.
# Using the User class from 9-3.

from tiy_nine_three import User

user_1 = User('Petrus', 'Rinto', 'Cloud Engineer', 'Global Reader')
user_2 = User('Bekkus', 'Plantus', 'Pharmacist', 'Global Healer')
user_3 = User('Bestus', 'Testus', 'Filler', 'Global Sealer')

users = [user_1, user_2, user_3]

for user in users:
    user.describe_user()
    user.greet_user()
    user.read_login_attempts()
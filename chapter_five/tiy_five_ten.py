# Patrick 13.10.2025.
# 5-10 Checking usernames.

current_users = ['admin', 'hamilton', 'guido', 'barry', 'lovelace']

new_users = ['turing', 'torvalds', 'guido', 'hopper', 'hamilton']

# Comparing users with a loop
for new_user in new_users:
    if new_user in current_users:
        print(f"Username '{new_user}' is taken, enter a new one!")
    else:
        print(f"Username '{new_user}' is available!")
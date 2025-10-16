# Patrick 13.10.2025.
# 5-10 Checking usernames.

current_users = ['admin', 'hamilton', 'guido', 'barry', 'lovelace']

new_users = ['turing', 'torvalds', 'guido', 'hopper', 'hamilton']

# Comparing users with a loop
for current_user in current_users:
    for new_user in new_users:
        if new_user.lower() in current_user.lower():
            print(f"Username '{new_user.title()}' is taken!")
        else:
            print(f"Username '{new_user.title()}' is available!")
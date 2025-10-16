# Patrick 16.10.2025.
# 5-10 Checking usernames.

# Existing users.
current_users = ['Admin', 'haMilTon', 'guIdO', 'barry', 'lOvelaCe']
# Copy list to lowercase with comprehension.
current_users_low = [user.lower() for user in current_users]
# New users.
new_users = ['turing', 'torvalds', 'guido', 'hopper', 'hamilton']

# Context in output.
print(f"\nCase sensitive list: {current_users}")
print(f"\nCase insensitive list: {current_users_low}\n")
print(f"\nNew users list: {new_users}\n")

# Comparing users with a loop.
print(f"\nOutput:")
for new_user in new_users:
    # case insensitive with lower().
    if new_user.lower() in current_users_low:
        print(f"Username '{new_user.title()}' is taken!")
    else:
        print(f"Username '{new_user.title()}' is available!")
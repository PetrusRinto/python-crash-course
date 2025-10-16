# Patrick 16.10.2025.
# 5-10 Checking usernames.

# Existing users.
current_users = ['Admin', 'haMilTon', 'guIdO', 'barry', 'lOvelaCe']
# New users.
new_users = ['TuriNG', 'TorvalDs', 'Guido', 'hoPPer', 'HaMilton']
# Copy lists to lowercase with comprehension.
current_users_low = [user.lower() for user in current_users]
new_users_low = [new_username.lower() for new_username in new_users]

# Context in output.
print(f"\nCase sensitive list: {current_users}")
print(f"\nCase insensitive list: {current_users_low}\n")
print(f"\nNew users sensitive list: {new_users}")
print(f"\nNew users insensitive list: {new_users_low}\n")

# Comparing users with a loop.
print(f"\nOutput:")
for new_user in new_users_low:
    if new_user in current_users_low:
        print(f"Username '{new_user.title()}' is taken!")
    else:
        print(f"Username '{new_user.title()}' is available!")
# Patrick 13.10.2025
# 5-8 Hello Admin.

# Username list.
usernames = ['admin', 'rufus', 'guido', 'barry', 'lovelace']

# User greeting.
for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, good to see you logged in again.")
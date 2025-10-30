# Patrick 30.10.2025.
# 7-5 Movie Tickets.

prompt = "\nHow old are you?"
prompt += "\n"

while True:
    age = input(prompt)
 
    if int(age) >= 12:
        print(f"\nYour ticket is $15.\n")
        break
    elif int(age) < 3:
        print(f"\nYour ticket is free!\n")
        break
    else:
        print(f"\nYour ticket is $10.\n")
        break
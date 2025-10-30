# Patrick 30.10.2025.
# 7-5 Movie Tickets. / 7-6 Three Exits.

prompt = "\nHow old are you?"
prompt += "\n"

active = True
while active == True:
    age = input(prompt)
 
    if int(age) >= 12:
        print(f"\nYour ticket is $15.\n")
    elif int(age) < 3:
        print(f"\nYour ticket is free!\n")
    else:
        print(f"\nYour ticket is $10.\n")
    active = False
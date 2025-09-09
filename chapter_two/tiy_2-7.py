userInput_1 = " tony"
userInput_2 = "stark "

firstName = userInput_1
lastName = userInput_2
quote = "I am Iron Man."

fullName = f"{firstName} {lastName}"
famousPerson = fullName.strip()

message = (f'"{quote}"\n\t- {famousPerson.title()}')

print(message)
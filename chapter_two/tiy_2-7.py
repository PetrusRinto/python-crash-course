# Patrick 10.09.2025
# A program that removes whitesaces and displays quotes in a appealing way

userInput_1 = " tony"
userInput_2 = "stark "

firstName = userInput_1
lastName = userInput_2
quote = "I am Iron Man."

fullName = f"{firstName} {lastName}"
famousPerson = fullName.strip()

message = (f'"{quote}"\n\t- {famousPerson.title()}')

print(message)
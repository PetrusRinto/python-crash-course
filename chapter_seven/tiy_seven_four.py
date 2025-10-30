# Patrick 30.10.2025.
# 7-4 Pizza Toppings.

# Prompting the user for input.
prompt = "\nEnter a topping for your pizza!"
prompt += "\nEnter 'quit' to end the program."
prompt += "\n: "

# Using a while loop for infinite toppings.
topping = ""
while topping != 'quit':
    topping = input(prompt)
    
    if topping != 'quit':
        print(f"\nI'll add {topping.lower()} to your pizza!")
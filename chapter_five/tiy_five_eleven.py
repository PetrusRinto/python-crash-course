# Patrick 16.10.2025.
# 5-11 Ordinal Numbers.

numbers = [numbers for numbers in range(1, 10)]

for num in numbers:
    if num > 3:
        print(f"{num}th\n")
    elif num == 3:
        print(f"{num}rd\n")
    elif num > 1:
        print(f"{num}nd\n")
    else:
        print(f"{num}st\n")
    
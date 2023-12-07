from utils.input import get_input_list

data = get_input_list(1)

print(data)

lines = data

digits = "0123456789"

first_digit = None
last_digit = None

total = 0

for line in lines:
    for char in line:
        if char in digits:
            if not first_digit:
                first_digit = char
            last_digit = char
    total += (int(first_digit + last_digit))
    first_digit = None
    last_digit = None

print(total)

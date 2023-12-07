
from utils.input import get_input_list

lines = get_input_list(1)

digits = "0123456789"
words = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


total = 0

for line in lines:
    first_digit = None
    last_digit = None
    current_string = ""
    for char in line:
        current_string_number = ""
        if char in digits:
            if not first_digit:
                first_digit = char
            last_digit = char
        else:
            current_string += char
            if current_string[-3:] in words:
                current_string_number = current_string[-3:]
            elif current_string[-4:] in words:
                current_string_number = current_string[-4:]
            elif current_string[-5:] in words:
                current_string_number = current_string[-5:]

            if current_string_number:

                if not first_digit:
                    first_digit = str(words[current_string_number])
                last_digit = str(words[current_string_number])

    total += (int(first_digit + last_digit))


print(total)

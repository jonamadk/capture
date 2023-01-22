import re


# Validate pass 1. 
# At least 8 characters,
# uppercase: A-Z,
# lowercase: a-z,
# numbers:0-9,
# speacial characters: @$%#!*&%

# Letters,numbers, speacial characters are optional



input_string = input("Enter anything \t")

result = lambda x: "Pass" if re.fullmatch('[A-Za-z0-9!@#$%^&*++]{8,}', x) else "Fail"

print(result(input_string))


import re

with open("skychallenge_accounting_input.txt", 'r') as f:
    data = f.read()

numbers_list = re.findall(r'[+-]?\d+(?:\.\d+)?', data)

numbers = [int(x) for x in numbers_list]

print("Sum of all numbers: ", sum(numbers))

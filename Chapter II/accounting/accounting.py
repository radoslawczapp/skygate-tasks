import re

# Define a path to the file
file_name = "skychallenge_accounting_input.txt"

# Open this file using context manager
with open(file_name, 'r') as f:
    # Save data from the file into the variable
    data = f.read()

# Create a list of numbers by using RegEx
numbers_list = re.findall(r'[+-]?\d+(?:\.\d+)?', data)

# Create a list of all numbers from the file by using list comprehension
numbers = [int(x) for x in numbers_list]

# Return the sum of all numbers from the file
print("Sum of all numbers: ", sum(numbers))

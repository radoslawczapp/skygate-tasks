import re


def get_sum(json_string):
    # Create a list of numbers by using RegEx
    numbers_list = re.findall(r'[+-]?\d+(?:\.\d+)?', str(json_string))

    # Create a list of all numbers from the file by using list comprehension
    numbers = [int(x) for x in numbers_list]
    # Return sum of these numbers
    return sum(numbers)


if __name__ == '__main__':
    # Define a path to the file
    file_name = "skychallenge_accounting_input.txt"
    # Open this file using context manager
    with open(file_name, 'r') as f:
        # Save data from the file into the variable
        f_data = f.read()
    # Return the sum of all numbers from the file
    print("Sum of all numbers: ", get_sum(f_data))

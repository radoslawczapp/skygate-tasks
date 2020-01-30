def check_valid_skyphrases(content):
    # Define a list of valid skyphrases
    valid_skyphrases = []

    for item in content:
        # Create a list of elements from each line
        item_list = item.split()
        # Create a set of the unique elements of each line
        item_set = set(item_list)

        # Compare these two data types, if they have a different length -> elements of the line are not unique
        if len(item_list) == len(item_set):
            # Fill a list with unique lines
            valid_skyphrases.append(item)
    # Return the length of unique lines, which is number of valid elements
    return len(valid_skyphrases)


if __name__ == '__main__':
    filename = 'skychallenge_skyphrase_input.txt'
    # Open a file using context manager in readable mode
    with open(filename, 'r') as f:
        # Save data from the file into the variable
        f_content = f.readlines()

    # Print the answer -> Number of valid skyphrases
    print("Number of valid skyphrases: ", check_valid_skyphrases(f_content))

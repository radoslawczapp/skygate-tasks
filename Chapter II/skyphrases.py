file_name = "skychallenge_skyphrase_input.txt"

with open(file_name, 'r') as f:
    file_content = f.readlines()

skyphrases = []

for line in file_content:
    skyphrases.append(line.strip())

valid_skyphrases = []

for item in skyphrases:
    item_list = item.split()
    item_set = set(item_list)

    if len(item_list) == len(item_set):
        valid_skyphrases.append(item)

print("Number of valid skyphrasees: ", len(valid_skyphrases))
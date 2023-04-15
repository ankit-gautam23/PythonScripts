import re

# Define n regular expressions in a list
regex_list = [re.compile(r'\d+'), re.compile(r'\d{3}'), re.compile(r'[a-z]+')]

# Open the text file and read its contents
with open('textfile.txt', 'r') as file:
    contents = file.read()

# Use the regular expressions to find matches in the text file
matches_list = [set(regex.findall(contents)) for regex in regex_list]

# Check if all sets of matches are equal
if all(matches == matches_list[0] for matches in matches_list):
    print('All regular expressions match the same statements in the text file')
else:
    print('Not all regular expressions match the same statements in the text file')

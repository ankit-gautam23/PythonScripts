import re
import os

# Define n regular expressions in a list
regex_list = [re.compile(r'\d+'), re.compile(r'\d{3}'), re.compile(r'[a-z]+')]

# Define a function to find matches in a file
def find_matches_in_file(file_path, regex_list):
    with open(file_path, 'r') as file:
        contents = file.read()
    return [set(regex.findall(contents)) for regex in regex_list]

# Define a function to compare sets of matches
def compare_matches(matches_list):
    return all(matches == matches_list[0] for matches in matches_list)

# Get a list of files in a directory
file_dir = '/path/to/directory/'
file_list = [os.path.join(file_dir, filename) for filename in os.listdir(file_dir)]

# Find matches in each file and compare sets of matches
all_matches = [find_matches_in_file(file_path, regex_list) for file_path in file_list]
if all(compare_matches(matches) for matches in all_matches):
    print('All regular expressions match the same statements in all files')
else:
    print('Not all regular expressions match the same statements in all files')

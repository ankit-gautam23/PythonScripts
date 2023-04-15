import re

# Define two regular expressions
regex1 = re.compile(r'\d+')
regex2 = re.compile(r'\d{3}')

# Open the text file and read its contents
with open('textfile.txt', 'r') as file:
    contents = file.read()

# Use the regular expressions to find matches in the text file
matches1 = set(regex1.findall(contents))
matches2 = set(regex2.findall(contents))

# Check if the sets of matches are equal
if matches1 == matches2:
    print('The two regular expressions match the same statements in the text file')
else:
    print('The two regular expressions do not match the same statements in the text file')

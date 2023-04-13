import re

special_char_regex = re.compile(r'[^\w\s]')
html_tags_regex = re.compile(r'<.*?>')
new_line_regex = re.compile(r'\n')
unwanted_spaces_regex = re.compile(r'\s+')

with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for line in input_file:
        line = special_char_regex.sub('', line)
        line = html_tags_regex.sub('', line)
        line = new_line_regex.sub(' ', line)
        line = unwanted_spaces_regex.sub(' ', line)
        output_file.write(line + '\n')

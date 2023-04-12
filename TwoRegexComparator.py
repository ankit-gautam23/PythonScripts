import re

regex1 = r"hello (world|universe)"
regex2 = r"hello (universe|world)"

if re.compile(regex1).pattern == re.compile(regex2).pattern:
    print("The two regular expressions are equivalent.")
else:
    print("The two regular expressions are not equivalent.")

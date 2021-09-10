import re

string = input()
# your code here
string_regex = re.match(r'^\+(\d)[\s-]?(\d{3})[\s-]?(\d{3}[\s-]?\d{2}[\s-]?\d{2})$', string)

if string_regex:
    print(f"Full number:  {string_regex[0]} ")
    print(f"Country code:  {string_regex[1]} ")
    print(f"Area code:  {string_regex[2]} ")
    print(f"Number:  {string_regex[3]} ")
else:
    print("No match")

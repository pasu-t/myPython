import re

# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'(\d{3}.){2}\d{4}') #simplified
pattern = re.compile(r'[89]00.\d\d\d.\d\d\d\d') #starts with 800 or 900


with open("data.txt", 'r') as f:
    content = f.read()
    matches = pattern.finditer(content)
    for match in matches:
        print(match)
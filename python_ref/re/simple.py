import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
mat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'^Start')
# pattern = re.compile(r'nd$')
# matches = pattern.finditer(sentence)

# for match in matches:
#     print(match)

# pattern = re.compile(r'[^b]at') #not starts with b and ends with at
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'(Mr|Mrs|Ms).?\s[A-Z]\w*')

pattern = re.compile(r'(Mr|Mrs|Ms).?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


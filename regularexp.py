import re

text_to_search =  '''abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
123-456-789

Ha HaHa

Metacharacters to be escaped
. ^ $ * + ? { } [ ] \ | ( )

citojaya.com

042-234-9822

'''

sentence = 'Start a senetence and then bring it to an end'

pattern = re.compile(r'\d\d\d\d\d\d\d\d\d\d')

matches = pattern.finditer(text_to_search)

for match in matches:
	print (match)

x = [4,5,6,7,8]
y = [i+1 for i in x]
print (y)

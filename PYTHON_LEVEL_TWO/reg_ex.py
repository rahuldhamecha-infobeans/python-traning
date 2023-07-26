import re

# find all contains one or more rd in the string
pattern = "rd+"
text = "rd.....rddddrd......rddddd...rdrdrd....rrrrrr"
match  = re.findall(pattern,text)
print(match) # Result : ['rd', 'rdddd', 'rd', 'rddddd', 'rd', 'rd', 'rd']

# find all contains zero or more rd in the string
pattern = "rd*"
text = "rd.....rddddrd......rddddd...rdrdrd....rrrrrr"
match  = re.findall(pattern,text)
print(match) # Result : ['rd', 'rdddd', 'rd', 'rddddd', 'rd', 'rd', 'rd', 'r', 'r', 'r', 'r', 'r', 'r']

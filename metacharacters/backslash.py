import re

string = 'github.com'

# tanpa backslash
match = re.search(r".", string)
print(match) # <re.Match object; span=(0, 1), match='g'>

# dengan backslash
match = re.search(r"\.", string)
print(match) # <re.Match object; span=(6, 7), match='.'>
import re

txt = "hello hello hello"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x) # ['hello']

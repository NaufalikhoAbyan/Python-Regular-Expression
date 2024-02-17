import re

txt = "hello hello hello"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x) # ['hello', 'hello', 'hello']

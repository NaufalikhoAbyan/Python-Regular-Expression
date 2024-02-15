import re

string = 'search inside of this text please!'

pattern = "[aiueo]"

match = re.findall(pattern, string)

print(match)
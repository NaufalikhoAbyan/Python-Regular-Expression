import re

string = 'search inside of this text please!'

match = re.search('this', string)

print(match)  # <_sre.SRE_Match object; span=(17, 21), match='this'>
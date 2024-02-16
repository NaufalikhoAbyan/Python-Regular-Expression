import re

txt = "The rain in Spain, But the s is silent"
x = re.findall("ai", txt)
print(x) # ['ai', 'ai']
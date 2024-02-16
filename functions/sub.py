import re

#Replace "rain" with "snow":

txt = "The rain in Spain"
x = re.sub("rain", "snow", txt)
print(x) # The snow in Spain

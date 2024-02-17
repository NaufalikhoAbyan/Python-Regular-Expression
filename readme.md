# Explorasi Regular Expression
## Penggunaan dasar regular expression dalam python
- Apa itu regular expression?  
Regular expression atau biasa disingkat "regex". regex digunakan untuk mendeteksi adanya atau tidak adanya suatu teks   

- Untuk menggunakan regex dalam python, kita harus menggunakan library 're' 
```py
import re
``` 

- Regex secara default akan mengembalikan span yang menujukan lokasi string yang cocok
```py
import re

string = 'search inside of this text please!'

match = re.search('this', string)

print(match)  # <_sre.SRE_Match object; span=(17, 21), match='this'>

print(match.start())  # 17
print(match.end())  # 21
``` 

## Regex Functions
Regex mempunyai beberapa function yang umum digunakan, diantaranya adalah: 
- findall : mengembalikan sebuah list yang cocok dengan string yang dicari
- search : mengembalikan sebuah objek jika ada suatu string yang cocok
- split : mengembalikan sebuah list dimana semua item telah dipisah berdasarkan string yang cocok
- sub : mengganti sebuah atau banyak string yang cocok

### Findall()
`findall.py`
```py
import re

txt = "The rain in Spain, But the s is silent"
x = re.findall("ai", txt)
print(x) # ['ai', 'ai']
```

### search()
`search.py`
```py
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 
# The first white-space character is located in position: 3
```

### split()
`split.py`
```py
import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) # ['The', 'rain', 'in', 'Spain']
```

### sub()
`sub.py`
```py
import re

#Replace "rain" with "snow":

txt = "The rain in Spain"
x = re.sub("rain", "snow", txt)
print(x) # The snow in Spain

```


## Regex Metacharacters 
Sebuah metacharacter adalah sebuah karater dengan fitur spesial. dibawah ini adalah daftar metacharacter yang digunakan oleh regex
- `\`     : digunakan untuk menghilangkan escape character
- `[]`    : merepresentasikan karakter class
- `^`     : mencocokan awalan teks
- `$`     : mencocokan akhiran teks
- `.`     : mencocokan semua karakter kecuali karakter yang berbeda baris
- `|`     : kondisional karakter untuk OR
- `?`     : tidak menemukan satupun teks yang cocok
- `*`     : menampilkan jumlah cocok (termasuk 0)
- `+`     : menampilkan jumlah cocok lebih dari 0
- `{}`    : memberi slot untuk diisi dengan karakter bebas

### 1. `\` - backslash  
backslash digunakan untuk menghilangkan fitur spesial yang mungkin dimiliki oleh sebuah karakter, contoh:
`backslash.py`
```py
import re

string = 'github.com'

# tanpa backslash
match = re.search(r".", string)
print(match) # <re.Match object; span=(0, 1), match='g'>

# dengan backslash
match = re.search(r"\.", string)
print(match) # <re.Match object; span=(6, 7), match='.'>
```
### 2. `[]` - Square Brackets
square brackets digunakan untuk mendefinisikan sebuah range, contoh:    
- `[abc]` akan mencocokan dengan karakter a, b, dan c 
- `[a-m]` akan mencocokan dengan karakter dari a sampai m  
- `[0-3]` akan mengambil karakter dari 0, 1, 2, dan 3   
kita bisa membalikan pencarian dengan menggunakan `^`   
- `[^a-m]` akan mencocokan dengan karakter selain a sampai m
- `[^0-3]` akan mencocokan dengan karaterk selain 0, 1, 2, dan 3    
contoh kode:
`squareBrackets.py`
```py
import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x) #['h', 'e', 'a', 'i', 'i', 'a', 'i']
```

### 3. `^` - Caret
Caret akan mengembalikan sebuah boolean jika string yang dicocokan merupakan string yang mengawali teks, contoh:
`caret.py`
```py
import re

txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
# Yes, the string starts with 'hello'
```

### 4. `$` - Dollar
Dollar akan mengembalikan sebuah boolean jika sring dicocokan merupakan string yang mengakhiri teks, contoh:
`dollar.py`
```py
import re

txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
# "Yes, the string ends with 'planet'"
```

### 5. `.` -Period
Period digunakan untuk mendefinisikan slot yang bebas untuk diisi oleh karakter apapun, period mengembalikan sebuah list, contoh:
`period.py`
```py
import re

txt = "hello hello hello"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x) # ['hello', 'hello', 'hello']
```

### 6. `*` - Asterisk
Asterisk digunakan untuk mendefinisikan slot yang bebas untuk diisi oleh karakter apapun, asterisk mengembalikan sebuah strig string di dalam list yang menggabungkan semua string ynag cocok contoh:
`asterisk.py`
```py
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x) # ['hello']
```

### 7. `+` - Plus
Plus digunakan untuk mendefinisikan slot yang bebas untuk diisi oleh karakter apapun, plus mengembalikan sebuah strig string di dalam list yang menggabungkan semua string ynag cocok contoh:
`plus.py`
```py
import re

txt = "hello hello hello"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.findall("he.+o", txt)

print(x) # ['hello hello hello']
```

### 8. `{}` - Curly Brackets
Curly brackets dapat digunakan untuk mendefinisikan slot yang dapat diisi oleh karakter bebas, contoh:
`curlyBrackets.py`
```py
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x) # ['hello']
```

### 9. `|` - Vertical Line
Vertical line digunakan untuk menambah teks alternatif untuk dicocokan, contoh:
`verticalLine.py`
```py
import re

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
# ['falls']
# Yes, there is at least one match!
```
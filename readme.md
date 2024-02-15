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
string = 'search inside of this text please!'

match = re.search('this', string)

print(match)  # <_sre.SRE_Match object; span=(17, 21), match='this'>

print(match.start())  # 17
print(match.end())  # 21
``` 

## Regex Metacharacters 
Sebuah metacharacter adalah sebuah karater dengan fitur spesial. dibawah ini adalah daftar metacharacter yang digunakan oleh regex
- `\`     : digunakan untuk menghilangkan escape character
- `[]`    : merepresentasikan karakter class
- `^`     : mencocokan awalan
- `$`     : mencocokan akhiran
- `.`     : mencocokan semua karakter kecuali karakter yang berbeda baris
- `|`     : kondisional karakter untuk OR
- `?`     : tidak menemukan satupun teks yang cocok
- `*`     : menampilkan jumlah cocok (termasuk 0)
- `+`     : menampilkan jumlah cocok lebih dari 0
- `{}`    : 
- `()`    :

### 1. `\` - backslash  
backslash digunakan untuk menghilangkan fitur spesial yang mungkin dimiliki oleh sebuah karakter, contoh:
```py
string = 'github.com'

# tanpa backslash
match = re.search(r".", string)
print(match) # <re.Match object; span=(0, 1), match='g'>

# dengan backslash
match = re.search(r"\.", string)
print(match) # <re.Match object; span=(6, 7), match='.'>
```
### 2. Square Brackets
square brackets digunakan untuk mendefinisikan sebuah range, contoh:    
- `[abc]` akan mencocokan dengan karakter a, b, dan c 
- `[a-m]` akan mencocokan dengan karakter dari a sampai m  
- `[0-3]` akan mengambil karakter dari 0, 1, 2, dan 3   
kita bisa membalikan pencarian dengan menggunakan `^`   
- `[^a-m]` akan mencocokan dengan karakter selain a sampai m
- `[^0-3]` akan mencocokan dengan karaterk selain 0, 1, 2, dan 3
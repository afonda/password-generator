import random

char_string = "!@#$%&1234567890qwertyuiopasdfghjklzxcvbnm?QWERTYUIOPASDFGHJKLZXCVBNM"

password = ""

for n in range(0, 14):
    password+=char_string[random.randint(0, len(char_string)-1)]
    
print(password)
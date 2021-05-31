import string
import random

def generatepass():
    password = ""
    specialchar = '!@#?]'
    alphabets = string.ascii_letters
    numbers = "01234567890"
    pool = alphabets + specialchar + numbers
    for i in range(5):
        aph3 = random.choice(alphabets)
        password += aph3
    for i in range(3):
        num3 = random.choice(numbers)
        password += num3
    for i in range(2):
        char2 = random.choice(specialchar)
        password += char2
    for i in range(5):
        aph3 = random.choice(alphabets)
        password += aph3
    return password

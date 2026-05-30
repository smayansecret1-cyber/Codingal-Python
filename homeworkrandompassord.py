import random

print("\n")

print("\n")

print("Welcome to the random passwrod app,we will suggest some strong passwords for you")

print("\n")

a = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

b = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

c = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

d = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '|',
    ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
    '`', '~'
]

pass1=""

for i in range (8):

    blu=random.randint(1,4)

    if blu == 1:
        pass1 += random.choice(a)

    elif blu == 2:
    
        pass1 += random.choice(b)

    elif blu == 3:
    
        pass1 += random.choice(c)

    elif blu == 4:
    
        pass1 += random.choice(d)

print(pass1)

print("\n")

pass2=""

for i in range (8):

    blu=random.randint(1,4)

    if blu == 1:
        pass2 += random.choice(a)

    elif blu == 2:
    
        pass2 += random.choice(b)

    elif blu == 3:
    
        pass2 += random.choice(c)

    elif blu == 4:
    
        pass2 += random.choice(d)

print(pass2)

print("\n")

pass3=""

for i in range (8):

    blu=random.randint(1,4)

    if blu == 1:
        pass3 += random.choice(a)

    elif blu == 2:
    
        pass3 += random.choice(b)

    elif blu == 3:
    
        pass3 += random.choice(c)

    elif blu == 4:
    
        pass3 += random.choice(d)

print(pass3)

print("\n")

pass4=""

for i in range (8):

    blu=random.randint(1,4)

    if blu == 1:
        pass4 += random.choice(a)

    elif blu == 2:
    
        pass4 += random.choice(b)

    elif blu == 3:
    
        pass4 += random.choice(c)

    elif blu == 4:
    
        pass4 += random.choice(d)

print(pass4)

print("\n")

pass5=""

for i in range (8):

    blu=random.randint(1,4)

    if blu == 1:
        pass5 += random.choice(a)

    elif blu == 2:
    
        pass5 += random.choice(b)

    elif blu == 3:
    
        pass5 += random.choice(c)

    elif blu == 4:
    
        pass5 += random.choice(d)

print(pass5)

print("\n")

print("\n")
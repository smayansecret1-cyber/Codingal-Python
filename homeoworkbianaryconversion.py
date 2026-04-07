print("\n")

print("\n")


print("Welcome to the Decimal to Binary Converter,enter decimal number and we will turn it into binary")

print("\n")

i = 1

num=float(input("Enter any decimal number you wnat to be converted :) :"))

num1=num

binary=""

while i <= 1:   # Outer loop


    while num > 0:   # Inner loop

        remainder = num % 2

        binary = str(remainder) + binary

        num = num // 2

    print("\n")

    print(f"{num1} in binary is {binary}")

    print("\n")

    i = i + 1

print("\n")

print("\n")
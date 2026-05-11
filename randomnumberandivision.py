import random

print("\n")

print("\n")

print("Welcome to the random number app,enter a range and we will chose a random number and tell if it's divisible by 13 ")

print("\n")

sn=int(input("Enter the starting number :) :"))

print("\n")

en=int(input("Enter the ending number :) :"))

print("\n")

def checker(a,b):

    ble=(random.randint(a,b))

    if (ble%13==0):

        print(ble,"is divisible by 13")

    else:

        print(ble,"is not divisible by 13")

checker(sn,en)

print("\n")

print("\n")
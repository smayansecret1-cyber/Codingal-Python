print("\n")

print("\n")

print("Welcome to the dividing app, enter a number and we will tellif a number is divisible by 13 , 6")

print("\n")

num=int(input("Enter a number :) :"))

print("\n")

def check(a):

    bleee=a%6

    blee=a%13

    if (bleee==0):

        if (blee==0):

            print("It is divible by both 6,13")

        else:

            print("It is only divisible by 6")

    elif (blee==0):

        print("It is only divisible by 13 ")

    else: 

        print("Its not divisible by neither 6 nor 13")

check(num)

print("\n")

print("\n")
print("\n")

print("\n")

print("Welcome to the even or odd app,enter a number and we will tell if it's odd or even ")

print("\n")

num=int(input("Enter a number :) :"))

print("\n")

def checker(a):

    ble=a%2

    if ble==0:

        return(True)
    
    else:

        return(False)

if checker(num):

    print("Its an even number")

else:

    print("Its and odd number")


print("\n")

print("\n")
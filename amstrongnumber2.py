print("\n")

print("\n")

print("welcome to the anmstrong number app,enter any number and we will tell if it's a amstrong number ")

print("\n")


num=int(input("enter the number you want to get checked :) : "))

print("\n")

sum=0

num1=num

while(num1>0):

    a=num1%10

    sum=sum+a**3

    num1=num1//10

if sum==num:

    print(f"{num} is a amstrong number")

else:

    print(f"{num} is not a amstrong number")

print("\n")

print("\n")
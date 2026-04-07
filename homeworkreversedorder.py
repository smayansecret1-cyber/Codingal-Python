print("\n")

print("\n")

print("Welcome to the counter app, enter any number and we will tell the number of digits it has ")

print("\n")

num=int(input("Enter the number you wanna get checked :) :"))

num1=num

print("\n")

counter=0

while(num>0):

    a=num%10

    num=num//10

    counter=counter+1

print(f"The number of digits in {num1} is {counter}")

print("\n")

print("\n")
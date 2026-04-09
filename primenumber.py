print("\n")

print("\n")

print("Welcome to the prime number app, enter the range and we will tell all the prime numbers in it")

print("\n")

ll=int(input("Enter the starting value :) :"))

print("\n")

counter=0

ul=int(input("Enter the end value :) :"))

for num in range(ll,ul+1):

    flag=0

    for i in range(2,num):

        if num%i==0:

            flag=1

            break

    if flag==0:

        print("\n",num)

        counter=counter+1

print(f"\n So there are {counter} prime numbers from {ll} to {ul}" )

print("\n")

print("\n")
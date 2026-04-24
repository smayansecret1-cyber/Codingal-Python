print("\n")

print("\n")

print("Welcome to the due app, enter the ifo adn we will tell how much you are due")

print("\n")

bill=float(input("Enter the total bill :) :"))

print("\n")

payed=float(input("Enter how much you paid :) :"))

print("\n")

def due(a,b):

    if a>b:

        print("You will get rupees",a-b,"back")

        print("\n")

    elif a<b:

        print("You are still due rupees",b-a)

        print("\n")

    elif a==b:

        print("You have payed fully")

        print("\n")

    else:

        print("IDK")

        print("\n")

due(payed,bill)

print("\n")

print("\n")
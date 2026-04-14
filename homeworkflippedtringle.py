print("\n")

print("\n")

print("Welcome to the tringle number app, enter the number of lines and we will make the partern")

print("\n")

ll=int(input("Enter the number of lines :) :"))

print("\n")

_num=0

for i in range(1, ll + 1):

    for space in range(ll - i, 0, -1):

        print(" ", end="\t")

    for j in range(1, i + 1):

        print("*", end="\t")

        _num=_num+1

    
    print("\n")

print("The number of charecters  in the tringle is :",_num)

print("\n")

print("\n")
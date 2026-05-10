print("\n")

print("\n")

print("Welcome to square it out !!,enter the range and we will tell all square numbers in that")

print("\n")

sn = int(input("Enter the starting number :) :"))

print("\n")

en = int(input("Enter the ending number :) :"))

print("\n")

even_list = []

odd_list = []

for i in range(sn, en + 1):

    l = i

    l = l * l

    if (l%2== 0):

        even_list.append(l)

    else:

        odd_list.append(l)

print("even square numbers are :", even_list)

print("\n")

print("odd square numbers are :", odd_list)

print("\n")

print("\n")
print("\n")

print("\n")

print("Welcome to the alphabetical app, enter the number of lines and we will genrate a alphabetical tringle")

print("\n")

line=int(input("Enter the number of lines :) :"))

imp=64

print("\n")

for i in range(1, line + 1):


    for j in range(1, i + 1):

        print(chr(imp+j), end="\t")


    print("\n")

print("\n")
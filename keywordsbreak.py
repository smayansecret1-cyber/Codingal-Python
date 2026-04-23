print("\n")

print("\n")

print("Welcome to the name checker app, enter the informtion and we will te;; if there is that letter")

print("\n")

name=input("Enter your name :) :")

print("\n")

letter=input("Enter the letter you want to find :) :")

print("\n")

for i in name.lower():

    if i==letter.lower():

        print(f"Letter {letter} is found")

        break

    else:

        print(f"Not found {letter}, currently on {i} \n \n")

print("\n")

print("\n")
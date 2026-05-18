print("\n")

print("\n")

print("WElcome to the reversed string app we will reverse a word or sometinhg you give and find how many vowls are there")

print("\n")

string=input("Enter the thing you want to check :) :")

print("\n")

string_=""

print("\n")

for  i in string:

    string_=i+string_

print(f"you wrote {string}")

print("\n")

print(f"REversed {string_}")

print("\n")

vowels=["a",'e',"i","o","u"]

count=0

for i.lower() in string_:

    if i in vowels :

        count=count+1

    else:

        continue

print(f"The number of vowels in {string_} is {count} ")

print("\n")

print("\n")
print("\n")

print("\n")

print("WElcome to the list comprehention app,enter a number and we will make a list of all odd and even numbers under it")

print("\n")

num=int(input("Enter the number :) :"))

print("\n")

list1=[]

list2=[]

for i in range (0,num+1):

    if i%2==0:

        list1.append(i)

    else:

        list2.append(i)

print(f"List of all even numbers under {num} :{list1} ")

print("\n")

print(f"List of all odd numbers under {num} :{list2} ")

print("\n")

print("\n")

print("Welcome to the futify app,we will capitalize the first letter of each fruit")

print("\n")

fruits=["watermelon","mango","apple","grapes","banana","litchi","musk melon","orange"]

print(f"current list {fruits}")

print("\n")

fruit=[]

for i in fruits:

    ref=i[0].upper() + i[1:]

    fruit.append(ref)

print(f"updated list {fruit}")

print("\n")
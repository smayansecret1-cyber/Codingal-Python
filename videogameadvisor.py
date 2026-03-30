print("\n")

print("\n")

print("Welcome to the permission app, Enter the information and we will tell can you play video games or not")

print("\n")

name=input("Enter your name :) :")

print("\n")

homework=input("Was there any homework given from shcool today, Y or N :) :")

print("\n")

if homework.lower()=="n":

    print(f"You can play video games {name}")

elif homework.lower()=="y":

    homeworkD=input("Is the homework given atlest done 80%, Y or N :) :")

    if homeworkD.lower()=="y":

        print(f" \n You can play video games {name}")

    elif homeworkD.lower()=="n":

        print(f" \n First do you home work {name}, then you can play")

else:

    print("Invalid input :(")

print("\n")

print("\n")
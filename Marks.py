print("\n")

print("\n")

print("Welcome to the maeks app, enter you marks and we will tell the avergae and the over all performance")

print("\n")

name=input("Enter the student's name :) :")

print("\n")

subject_1=input("Enter the first subject")

print("\n")

subject_1_Marks=float(input(f"Enter the marks of {subject_1}"))

print("\n")

subject_2=input("Enter the second subject")

print("\n")

subject_2_Marks=float(input(f"Enter the marks of {subject_2}"))

print("\n")

subject_3=input("Enter the third subject")

print("\n")

subject_3_Marks=float(input(f"Enter the marks of {subject_3}"))

print("\n")

subject_4=input("Enter the forth subject")

print("\n")

subject_4_Marks=float(input(f"Enter the marks of {subject_4}"))

print("\n")

average=(subject_1_Marks + subject_2_Marks + subject_3_Marks + subject_4_Marks)/4

if average>90:

    print(f"Very good {name} your average is {average}")

    print("\n")

    print("Very good performance")

elif average>80:

    print(f"Good {name} your average is {average}")

    print("\n")

    print("Good performace")

elif average>70:

    print(f"Nice try {name} your average is {average}")

    print("\n")

    print("Average")

elif average<70:

    print(f"{name} your average is {average}")

    print("\n")

    print("Need to improve")

else :

    print(":(")

print("\n")

print("\n")
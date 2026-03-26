print("\n")

print("\n")

medical_condition= input("Did you have medical condition? Y or N ")

print("\n")

if (medical_condition.lower()== 'y'):

    print("You are eligible to take the test")

elif medical_condition.lower()=='n':

    attend= float(input("\n Enter you attendance percentage? "))

    if attend>=75.0:

        print("You are eligible to take the test")

    else:

        print("You are not eligible because of low attendance ")

else:

    print("Wrong input")

print("\n")

print("\n")
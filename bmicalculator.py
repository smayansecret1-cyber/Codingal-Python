print("\n")

print("\n")

print("Welcome to the bmi calculator, enter the info and find about your self ")

print("\n")

height = float(input("Enter your height in m :) : "))

print("\n")

weight = float(input("Enter your weight in kg :) : "))

print("\n")

BMI = weight / (height)**2

print("Your BMI is",BMI)

if BMI <= 18.4:

    print("You are underweight.")


elif BMI <= 24.9:

    print("You are healthy.")


elif BMI <= 29.9:

    print("You are over weight.")


elif BMI <= 34.9:

    print("You are severely over weight.")


elif BMI <= 39.9:
    print("You are obese.")


else:

    print("You are severely obese.")

print("\n")

print("\n")
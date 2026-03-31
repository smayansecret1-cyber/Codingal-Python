print("\n")

print("\n")

print("Welcome to the Power Calculator, enter the number and the power and we will tell its answer")

print("\n")

number = int(input("Enter the number :) : "))

print("\n")

power = int(input("Enter the power :) : "))

print("\n")

result = 1

for i in range(power):
    result = result * number

print(f"{number} to the power {power} is {result}")

print("\n")

print("\n")
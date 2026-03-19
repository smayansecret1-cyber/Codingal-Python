print("\n")

print("\n")

print("Welcome to the budget app enter your budget and we will tell you if you can buy that item")

print("\n")

budget=int(input("Enter your budget :) :"))

print("\n")

price=int(input("Enter the cost of the item :) :"))

print("\n")

if budget>price:
    print("You can by it and be left with",budget-price)

else:
    print("You will not be able to buy it, you are just short of ",price-budget)

print("\n")

print("\n")
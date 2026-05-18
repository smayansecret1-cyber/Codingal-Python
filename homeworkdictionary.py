print("\n")

print("\n")

print("Welcome to the frequency app,enter the value you want to check andwe will tell how many times does it come in the dictionary")

print("\n")

test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print("The original dictionary : " + str(test_dict))

print("\n")

K = input("Enter what you want to check :) :")

print("\n")

count = 0

for key,value in test_dict.items():

    if value==2:

        count+=1

print(f"Frequency of {K} is {count}")

print("\n")

print("\n")
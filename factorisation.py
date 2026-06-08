print("\n")

print("\n")

print("Welcome to the factor app,we will tell the factor a of a number")

print("\n")

num=int(input("Enter a number whose factors you wanna know:) :"))

print("\n")

factors=[]

for i in range (1,num+1):

    if num%i==0:
        
        factors.append(i)

print(f"The factors of {num} are :{factors}")

print("\n")

print("\n")
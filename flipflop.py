print("\n")

print("\n")

print("Welcome to the flip flop app,we will tell if the tupple is a palindrome or not")

print("\n")

tuple1= (1,2,3,3,2,1)

i=0

j=len(tuple1)-1

flag=0

while(i<len(tuple1)):

    if tuple1[i]!= tuple1[j]:

        flag=1

        break

    i+=1

    j-=1

if flag==0:

    print("It is palindrome")

else:

    print("No it is not")

print("\n")

print("\n")
print("\n")

print("\n")

print("welcome to the armstrong nnummber app, we will tell you all the armstrong  nnumbers from 100-1000")

print("\n")

counter=0

num=0

sum=0

num1=num

while (counter<1001):

     while(num1>0):

        a=num1%10

        sum=sum+a**3

        num1=num1//10

        if sum==num:

            print(f"{num} is a amstrong number \n \n")

        else:
             
            continue

        counter=counter+1


        num=num+1

            
print("\n")

print("\n")
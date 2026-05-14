print("\n")

print("\n")

print("WEcome to the even and divide app,enter the range and we will do it")

print("\n")

sn=int(input("Enter the staring number :) :"))

print("\n")

en=int(input("Enter the ending number :) :"))

print("\n")

even=[]

if (en>sn):

    for i in range (sn,en+1):

        j=i

        if (j%2==00):

            if (i%6==00):

                continue

            else:

                even.append(j)

        else:

            continue

else:

    for i in range (sn,en,-1):

        j=i

        if (j%2==00):

            if (i%6==00):

                continue

            else:

                even.append(j)

        else:

            continue

print(even)

print("\n")

print("\n")
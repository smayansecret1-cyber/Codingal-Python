print("\n")

print("\n")

n = 100

while (n <= 1000):

    sum = 0

    n1 = n

    while (n1 > 0):

        a = n1 % 10

        sum = sum + a ** 3

        n1 = n1 // 10

    if sum == n:

        print(n,"\n \n")

    n += 1

print("\n")

print("\n")
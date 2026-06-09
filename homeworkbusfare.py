print("\n")

print("\n")

print("Welcome to the bus fare calculator,we will help you calculate your bus fare")

print("\n")


class Vehicle:

    def __init__(self, capacity):

        self.capacity = capacity

    def fare(self):

        return self.capacity * 100


class Bus(Vehicle):

    def fare(self):

        fare = super().fare()

        fare2 = fare * 0.10

        total = fare + fare2

        return total


num = int(input("Enter total capacity of the bus :) :"))

print("\n")

blee = Bus(num)

print(f"So total fare is {blee.fare()}")

print("\n")

print("\n")
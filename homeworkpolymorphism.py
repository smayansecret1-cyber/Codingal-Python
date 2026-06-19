print("\n")

print("\n")

print("Welcome to the car app, we will tell about cars")

print("\n")

class ferrari():

    def __init__(self,topspeed,price):

        self.topspeed= topspeed

        self.price= price

    def display(self):

        print("ferrari")

        print("\n")

        print(f"Top Speed    :    {self.topspeed}")

        print("\n")

        print(f"price        :    {self.price}")

        print("\n")

class BMW():

    def __init__(self,topspeed,price):

        self.topspeed= topspeed

        self.price= price

    def display(self):

        print("BMW")

        print("\n")

        print(f"Top Speed    :    {self.topspeed}")

        print("\n")

        print(f"price        :    {self.price}")

        print("\n")      

car1=ferrari("350 km/h","$500,000")

car2=BMW("250 km/h","$75,000")

car1.display()

print("\n")

car2.display()

print("\n")

print("\n")

print("\n")
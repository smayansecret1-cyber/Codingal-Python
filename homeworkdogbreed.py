print("\n")

print("\n")

print("Welcome to the dog breed app,we will tell about some dog breeds")

print("\n")

print("\n")

class dog:

    def __init__(self, breed, colour, type):

        self.breed = breed

        self.colour = colour

        self.type = type

    def display(self):

        print(f"Breed : {self.breed}")

        print("\n")

        print(f"Colour : {self.colour}")

        print("\n")

        print(f"Type : {self.type}")

        print("\n")

a = dog("Labrador Retriever", "Yellow, Black, Chocolate Brown", "Very Friendly")

b = dog("Golden Retriever", "Golden, Cream", "Very Friendly")

c = dog("German Shepherd", "Black & Tan, Black, Sable", "Protective")

d = dog("Beagle", "Black, White, Brown", "Friendly")

e = dog("Pug", "Fawn, Black", "Friendly")

a.display()

print("\n")

b.display()

print("\n")

c.display()

print("\n")

d.display()

print("\n")

e.display()

print("\n")

print("\n")
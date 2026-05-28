print("\n")

print("\n")

print("Welcome to the birding app,we will tell the names and age of the parrts we found")

print("\n")

class Parrot:

    species = "bird"

    def __init__(self, name, age):

        self.name = name

        self.age = age

blu = Parrot("Blu", 10)

woo = Parrot("Woo", 15)

print("Blu is a {}".format(blu.species))

print("\n")

print("Woo is also a {}".format(woo.species))

print("\n")

print("{} is {} years old".format( blu.name, blu.age))

print("\n")

print("{} is {} years old".format( woo.name, woo.age))

print("\n")

print("\n")
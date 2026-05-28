print("\n")

print("\n")

print("WElcome to the class and obj app,we will tell the taste , color , and name of the fruit")

print("\n")

class fruit:

    taste = 'Sweet'

    def __init__(self, name, color):

        self.name = name

        self.color = color

apple = fruit('Apple', 'Red')

banana = fruit('Banana', 'Yellow')

print(apple.taste)

print("\n")

print(apple.name, apple.color)

print("\n")

print(banana.name, banana.color)

print("\n")

print("\n")
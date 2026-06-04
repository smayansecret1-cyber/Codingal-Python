print("\n")

print("\n")

print("Welcome to the employ roaster,we will tell the details about the employ")

print("\n")

class Employ():

    def __init__(self,name,id_number):

        self.name= name

        self.id_number= id_number

    def display(self):

        print(self.name)

        print("\n")

        print(self.id_number)

        print("\n")

class Person(Employ):

    def __init__(self,name,id_number,salary,post):

        super().__init__(name,id_number)

        self.salary= salary

        self.post= post


a = Person("mohan","245","1,25,000","Senoir Dev")

a.display()

print(a.salary)

print("\n")

print(a.post)

print("\n")

print("\n")
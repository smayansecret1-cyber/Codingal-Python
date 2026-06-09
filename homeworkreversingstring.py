print("\n")

print("\n")

print("Welcome to the reversed word app,enter something and we will reverse it")

print("\n")

class reverse:

    def __init__(self, s=""):

        self.s = s

    def reverse_string(self):

        return self.s[::-1]

word=input("enter what you want to reverse :) :")

print("\n")

reversed= reverse(word)

print("the reversed form is:", reversed.reverse_string())

print("\n")

print("\n")
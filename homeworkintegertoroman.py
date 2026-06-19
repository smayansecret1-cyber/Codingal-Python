print("\n")

print("\n")

print("Welcome to the roman converter app, we will convert numbers in to roman numbers")

print("\n")

num=int(input("Enter the number you want to convert :) :"))

print("\n")

class RomanConverter:

    def __init__(self, number):

        self.number = number

    def convert(self):

        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        answer = ""

        for i in range(len(values)):

            while self.number >= values[i]:\

                answer += roman[i]

                self.number -= values[i]

        return answer


obj = RomanConverter(num)

print("Roman Numeral:", obj.convert())

print("\n")

print("\n")
import turtle

turtle.Screen().bgcolor("orange")

turtle.Screen().setup(300,400)

polygon = turtle.Turtle()

num_sides = 4

side_length = 70

angle = 90

polygon.speed(1)

for i in range(num_sides):

    polygon.forward(side_length)

    polygon.right(angle)

turtle.done()
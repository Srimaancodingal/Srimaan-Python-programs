import turtle
turtle.Screen().bgcolor("Yellow")
turtle.Screen().setup (1000, 1000)
polygon = turtle.Turtle()
polygon.pensize(6)
sides = int(input("Enter the number of sides : "))
length_of_sides = 100
angle = 360.0/sides
for i in range (sides):
    polygon.forward (length_of_sides)
    polygon.right (angle)
turtle.done()

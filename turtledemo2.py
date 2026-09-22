import turtle
turtle.Screen().bgcolor ("Orange")
turtle.Screen().setup (1000, 1000)
star = turtle.Turtle()
sides = 3
angle = 120 
length_of_sides = 200
for i in range (sides):
    star.forward (length_of_sides)
    star.left (angle)
star.penup()
star.left (90)
star.forward (100)
star.right (90)
star.pendown ()
for i in range (sides):
    star.forward (length_of_sides)
    star.right (angle)
turtle.done()



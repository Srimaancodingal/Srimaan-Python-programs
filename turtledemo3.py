import turtle
turtle.Screen().bgcolor ("Orange")
turtle.Screen().setup (1000, 1000)
star = turtle.Turtle()
size = 0 
while True:
    for i in range (4):
        star.forward (size+1)
        star.left (90)
        size = size - 5
    size = size + 1 
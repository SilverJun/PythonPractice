import turtle

t = turtle.Turtle()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

def drawPoly(sideLength, numSides, color):
    t.color(color)
    turnAngle = 360/numSides
    for i in range(numSides):
        t.pendown()
        t.forward(sideLength)
        t.right(turnAngle)

for i in range(3):
    t.penup()
    t.setposition(40*i, 0)
    drawPoly(20, 6, colors[i])

for i in range(5):
    t.penup()
    t.setposition(40*(i-2), -100)
    drawPoly(40, 4, colors[i])

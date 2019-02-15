import turtle

def square(t, size, color):
    t.color(color)
    for i in range(4):
        t.forward(size)
        t.right(90)

t1 = turtle.Turtle()
t1.pensize(3)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

i=30
for color in colors:
    square(t1, i, color)
    i=i+30


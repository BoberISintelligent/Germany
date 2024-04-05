import turtle

screen = turtle.Screen()
t = turtle.Turtle()

t.color("Black")
t.pensize(50)

for _ in range(4):
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(180)

t.hideturtle()
screen.mainloop()

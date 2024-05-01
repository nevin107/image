import turtle
flag_turtle=turtle.Turtle()


flag_turtle.penup()
flag_turtle.goto(0, 0)
flag_turtle.pendown()
flag_turtle.color("navy")
flag_turtle.pensize(4)

# Draw the outer circle
flag_turtle.circle(50)

# Draw the 24 spokes
for _ in range(24):
    flag_turtle.penup()
    flag_turtle.goto(0, 50)
    flag_turtle.pendown()
    flag_turtle.forward(50)
    flag_turtle.backward(50)
    flag_turtle.left(360 / 24)

turtle.done()    
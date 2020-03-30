import turtle

turtle.color('red', 'yellow')
turtle.begin_fill()

while True:
    turtle.forward(200)
    turtle.left(170)

    if abs(turtle.pos()) < 1:
        break

turtle.circle(80)
turtle.end_fill()
turtle.done()

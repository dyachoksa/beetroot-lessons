import turtle


def draw_circle(r):
    if r > 400:
        print ('Слишком большой радиус ')
        return
    elif r < 1:
        print ('Слишком маленький радиус ')
        return

    turtle.circle(r)
    turtle.left(180)
    turtle.circle(r*2)
    turtle.done()


if __name__ == "__main__":
    userInput = int(input('Введите радиус: '))
    draw_circle(userInput)

import turtle

def draw_snowman(r: int, color="yellow"):
    if r < 1 or r > 400:
        print('Invalid radius')
        return
    
    turtle.color('red', color)
    turtle.begin_fill()
    for c_r, c_s in [(r//2, 2*r), (r, 0), (r*2, -(2*r+2*r))]:
        turtle.penup()
        turtle.setpos((0, 0))
        turtle.sety(c_s)
        turtle.pendown()
        turtle.circle(c_r)
    
    turtle.end_fill()
    turtle.done()
    

def draw_circle(radius):
    if radius <1 or radius > 400:
        print('Invalid radius')
        return None
    
    turtle.color('red','yellow')
    
    circle_step=0.2
    for i in range(0,3):
        turtle.penup()
        rad=radius*(1+circle_step*i)
        y_pos=turtle.ycor()-rad*2
        turtle.sety(y_pos)
        turtle.pendown()
        turtle.circle(rad)
    
    turtle.end_fill()
    turtle.done()

if __name__ == '__main__' :
    turtle.setup(1920, 1080)
    r = turtle.numinput('Snowman', 'Enter radius: ', 50)
    draw_snowman(r, "green")

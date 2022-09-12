import turtle

screen = turtle.Screen()

t = turtle.Turtle()


def Draw_Rect(Hight,width,color):
    t.down()
    t.fillcolor(color)
    t.begin_fill()

    t.right(90)
    t.forward(Hight)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(Hight)
    t.left(90)
    t.forward(width)

    t.end_fill()
    t.up()

def Draw_tri(Hight, Width,color):
    t.down()
    t.fillcolor(color)
    t.begin_fill()

    t.right(135)    
    t.forward(Hight)

    t.right(90)
    t.forward(Hight)

    t.right(135)
    t.forward(Width)

    t.end_fill()
    t.up()   

def Draw_circ(size, color):
    t.down()
    t.fillcolor(color)
    t.begin_fill()

    t.circle(size)

    t.end_fill()

def turtle_state():
    var1= t.isdown()
    var2 = t.heading()
    varX = t.xcor()
    varY = t.ycor()
    print(var1 , var2 , varX , varY)

def main():
    t.up()
    t.goto(-250,0)
    Draw_Rect(150,100,"spring green")
    Draw_tri(70,100,"firebrick")
    turtle_state()

    t.goto(-100,-50)
    t.right(180)
    Draw_Rect(100,150,'cyan')
    Draw_tri(105,150,'firebrick')


    t.right(180)
    t.goto(100,50)
    Draw_Rect(200,30,'firebrick')

    t.right(180)
    t.forward(15)
    t.right(90)
    t.forward(10)
    t.left(90)
    Draw_circ(80, "lime green")


main()

turtle.mainloop()

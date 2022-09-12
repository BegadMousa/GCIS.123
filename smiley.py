from lib2to3.pgen2 import driver
import turtle

t = turtle.Turtle()

def Draw_circle(x_cord , y_cord, rad, color):
    t.up()
    t.goto(x_cord, y_cord)
    t.fillcolor(color)
    t.begin_fill()

    t.down()
    t.circle(rad)

    t.end_fill()

def Draw_centered_circle(x ,y, rad, color):
    t.up()
    t.goto(x,y)
    t.forward(rad)
    t.left(90)

    t.pencolor("black")
    t.fillcolor(color)

    t.down()
    t.begin_fill()
    t.circle(rad)
    t.end_fill()
    t.up()
    
    t.left(90)
    t.forward(rad)
    t.right(180)
    


def Draw_smiley(x,y,rad,color):
    Draw_centered_circle(x,y,rad,"yellow")

    # nose
    Draw_centered_circle(x,y,rad/10,"red")

def main():
    Draw_smiley(0,0,200,"yellow")
    input("...")
    

main()

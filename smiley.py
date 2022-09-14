from lib2to3.pgen2 import driver
import turtle

t = turtle.Turtle()

def Draw_circle(x_cord, y_cord, rad, color):
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
    Draw_centered_circle(x,y,rad/10,"red") #nose

    quarter = rad/4
    tenth = rad /10
    Draw_eye(x+quarter+tenth, y+quarter, quarter, "blue")
    Draw_eye(x-quarter-tenth, y+quarter, quarter, "blue")


def Draw_eye(x,y,radius, eye_color):
    Draw_centered_circle(x,y,radius,"white")
    Draw_centered_circle(x,y,radius/2, eye_color)
    Draw_centered_circle(x,y,radius/4, "black")

def Tweek(speed,tracer):
    t.speed(speed)
    # t.tracer(tracer)

def main():
    Tweek(0,False)
    Draw_smiley(0,0,200,"yellow")
    input("...")
    

main()

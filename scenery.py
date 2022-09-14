import turtle

# init
screen = turtle.Screen()
t = turtle.Turtle()

# global var
big_facade = 0
sm_facade = 0

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

    t.right(180)

    t.end_fill()
    t.up()

def Draw_tri(Hight, Width,color):
    t.down()
    t.fillcolor(color)
    t.begin_fill()

    t.left(45)   
    t.forward(Hight)

    t.right(90)
    t.forward(Hight)

    t.right(135)
    t.forward(Width)

    t.right(180)

    t.end_fill()
    t.up()   

def Draw_centered_circle(x ,y, rad, color):
    t.up()
    t.goto(x,y)
    t.forward(rad)
    t.left(90)

    t.fillcolor(color)

    t.down()
    t.begin_fill()
    t.circle(rad)
    t.end_fill()
    t.up()
    
    t.left(90)
    t.forward(rad)
    t.right(180)

def Draw_house(x,y,hight, width, roof_hight, story, window_size,door_h,door_w, color_house,color_roof, window_color, door_color):
    global big_facade, sm_facade
    t.goto(x,y)

    Draw_Rect(hight,width, color_house)     
    Draw_tri(roof_hight, width, color_roof)

    half = width / 2
    quarter = width / 4
    eighth = width / 8
    sixenth = width /16

    t.up()
    t.goto(x+quarter ,y - hight/4)
    Draw_Rect(window_size,window_size, window_color)

    t.goto(x+half+eighth, y - hight/4)
    Draw_Rect(window_size,window_size, window_color)

    if story == 2:
        t.goto(x+quarter ,y - hight/2)
        Draw_Rect(window_size,window_size, window_color)

        t.goto(x+half+eighth ,y - hight/2)
        Draw_Rect(window_size,window_size, window_color)

    t.goto(x+half-door_w/2, y-hight+door_h)
    Draw_Rect(door_h,door_w, door_color)

    if big_facade < hight * width:
        big_facade = hight * width

    if hight * width < big_facade:
        sm_facade = hight * width

def Draw_tree(x,y, hight, width , rad, truck_color, leafs_color):
    t.goto(x,y)
    Draw_Rect(hight, width, truck_color)
    Draw_centered_circle(115+width/2,50 ,rad, leafs_color)

# debug function
def turtle_state():
    var1= t.isdown()
    var2 = t.heading()
    varX = t.xcor()
    varY = t.ycor()
    print(var1 , var2 , varX , varY)

def main():
    t.speed(0)
    t.up()

    Draw_house(-100,-50,100,180,127,1,25,25,25,"light slate gray", "firebrick","light sky blue","saddle brown")

    Draw_house(-250,0,150,100,70, 2, 15,25,15,"spring green", "firebrick", "light sky blue", "saddle brown")

    Draw_tree(115 ,50 ,200 ,30 , 80 ,"firebrick" ,"lime green" )

    t.goto(-400, 300)
    t.write("by Begad, Hesham and Sufian", font=('Arial', 16, 'normal')) 


    print(f'Big Facade is {big_facade} square "units"')
    print(f'Small Facade is {sm_facade} square "units"')
    input('Press any key to QUIT ...')

main()

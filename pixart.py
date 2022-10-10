import turtle

PIXEL_SIZE = 30
ROWS=20
COLUMNS=20

def init():
    turtle.speed(0)
    turtle.up()
    turtle.goto(-200,200)
    turtle.pencolor("black")
    turtle.fillcolor("cyan")
    turtle.pensize(1)

def Draw():
    i = 0

    turtle.begin_fill()
    turtle.down()

    while i<4:
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
        i += 1

    turtle.up()
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)

def pixart_move(row,col):
    xcor = -200
    ycor = 200
    turtle.goto(xcor,ycor)      
    xcor += PIXEL_SIZE * col
    ycor += PIXEL_SIZE * row
    turtle.goto(xcor,ycor)


def draw_row(row,col,num_pixels,color="red"):
    xcor = -200
    ycor = 200

    xcor += PIXEL_SIZE*col
    ycor += PIXEL_SIZE*row
    turtle.goto(xcor,ycor)
    turtle.fillcolor(color)
    
    i=0
    print(1)
    for i in range(num_pixels):
        Draw() 


def main():
    init()
    # Draw()
    draw_row(5,0,20)
    

if __name__ == "__main__":
    main()
    input("Press Enter to quit....")
    print("baguette") 



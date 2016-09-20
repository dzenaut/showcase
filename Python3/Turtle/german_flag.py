from turtle import *

def rectangle(pen, rect):
    '''draws a rectangle, position on y axis depends on nth rectangle'''
    y = (-101)*(int(rect)-1)
    position = (-200, y)
    pen.up()
    pen.goto(position)
    pen.down()
    for i in range(2):
        pen.forward(100)
        pen.left(90)
        pen.forward(400)
        pen.left(90)

#set color of pens
pen1 = Pen()

pen2 = Pen()
pen2.pencolor('#FF0000')
pen2.fillcolor('#FF0000')

pen3 = Pen()
pen3.pencolor('#FFD700')
pen3.fillcolor('#FFD700')

#make first rectangle and fill black
pen1.setheading(270)
pen1.begin_fill()
rectangle(pen1, 1)
pen1.end_fill()


#move to starting position for second rectangle
#pen2.goto(0, -101)

#make second rectangle and fill red
pen2.setheading(270)
pen2.begin_fill()
rectangle(pen2, 2)
pen2.end_fill()

#move to starting position for third rectangle
#pen3.goto(0,-202)

#make third rectangle and fill gold
pen3.setheading(270)
pen3.begin_fill()
rectangle(pen3, 3)
pen3.end_fill()

#hide turtles
pen1.hideturtle()
pen2.hideturtle()
pen3.hideturtle()

mainloop()







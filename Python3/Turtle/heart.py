import turtle

#initiate pen
pen1 = turtle.Pen()

#set color of pen
pen1.pencolor('#FF0000')
pen1.fillcolor('#FF0000')

pen1.up()
pen1.goto(0, -200)
pen1.down()

#begin filling
pen1.begin_fill()

#orient turtle to move up/left in 45° and move
pen1.setheading(135)
pen1.forward(250)

#set up direction for first half circle
pen1.setheading(315)

#draw two semicircles
pen1.circle(125,-180)
pen1.setheading(225)
pen1.circle(125,-180)

#draw line 45° down/left
pen1.setheading(225)
pen1.forward(250)

#end filling
pen1.end_fill()

#hide turtle
pen1.hideturtle()

#to keep window open after drawing is finished
turtle.mainloop()


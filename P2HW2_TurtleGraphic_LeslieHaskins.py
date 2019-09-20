#Use Turtle Graphics to Draw Two Triangles
#9/20/19
#CTI-110 P2HW2-Turtle Graphic
#Leslie Haskins

#Open Turtle Graphics in Python
#Input commands to make Turtle draw a triangle
#Input commands to add color to next triangle to be drawn
#Input commands to make Turtle draw a second triangle inside first triangle
#Display the graphics 


import turtle #Display graphic in window
turtle.showturtle() 

turtle.penup #pick pen up off paper

turtle.backward(250) #move pen backward 250 pixels

turtle.pendown() #place pen down

turtle.forward(500) #move graphic forward 500 pixels

turtle.left(120) #turn graphic to left 120 degrees

turtle.forward(500) #move graphic forward 500 pixels

turtle.left(120)  #turn graphic to left 120 degrees

turtle.forward(500)#move graphic forward 500 pixels

turtle.left(120)#turn graphic to left 120 degrees


turtle.fillcolor("blue") #add color to shape
turtle.begin_fill()

turtle.forward(500) #move graphic forward 500 pixels

turtle.left(140) #turn graphic to left 140 degrees

turtle.forward(320) #turn graphic forward 320 pixels

turtle.left(79) #turn graphic to left 79 degrees

turtle.forward(327) #move graphic forward 327 pixels

turtle.end_fill() #end colorfill



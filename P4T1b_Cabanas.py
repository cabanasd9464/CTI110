# Drawing my initials
# March 18, 2019
# CTI-110 P4T1 - Initials
# Drake Cabanas
# 

import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(3)            # increase pensize (takes integer)
t.pencolor("blue")     # set pencolor (takes string)
t.shape("turtle")


# Have turtle draw a D
t.right(90)
t.forward(150)
t.left(90)
t.forward(30)
t.left(37.5)
for i in range (4):
    t.forward(50)
    t.left(37.5)
t.forward(30)

# Have turtle move and draw a C
t.penup()
t.right(8)
t.backward(220)
t.pendown()
for i in range (6):
    t.forward(50)
    t.left(37.5)



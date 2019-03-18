# Drawing two shapes
# March 18, 2019
# CTI-110 P4T1 - Turtle Graphics
# Drake Cabanas
# 

import turtle             # Allows us to use turtles
win = turtle.Screen()      # Creates a playground for turtles
t = turtle.Turtle()    # Create a turtle, assign to t

# Tell turtle to draw a square
for i in range (4):
    t.forward(50)
    t.left(90)

# Tell turtle to move so shapes do not overlap
t.penup()
t.forward(100)
t.pendown()

# Tell turtle to draw a triangle
for i in range (3):
    t.forward(100)
    t.left(120)
    
# end commands
win.mainloop()             # Wait for user to close window

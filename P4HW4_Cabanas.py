# Creating a star using a nested loop
# March 18, 2019
# CTI-110 P4HW4 - Nested Loops
# Drake Cabanas
#

def main():
    
    import turtle          # Allows us to use turtles
    win = turtle.Screen()  # Creates a playground for turtles
    t = turtle.Turtle()    # Create a turtle, assign to t
    t.pensize(4)           # Sets pen size
    t.pencolor("red")      # Sets pen color
    t.shape("turtle")      # Sets pen shape

    t.right(180)

    # Tell turtle to draw an octagon
    for i in range (8):
        # Tell turtle to draw a triangle
        for l in range(3):
            t.forward(100)
            t.right(120)
        t.forward(100)
        t.left(45)
# Program start
main()

#Jose Rodriguez
#10/26/2026
#P4LAB1
# Use turtle and loops to draw a square and a triangle
# Do not forget instructions want the triangle on top of the square.
# I had to google how to fill the triangle with color, i verify all the material and video tutorials and the information was not provided or i could not find it.

# Import the library
import turtle

# Create the turtle window and drawing 0object, this is the external window that opens when you hit run.
# This window shows the working of the turtle and the shapes that are drawn.
win = turtle.Screen()
pen = turtle.Turtle()



#^^ This is the pen use to draw the shapes.
# Set turtle options
pen.pensize(5)
pen.pencolor ("purple")
pen.shape("arrow")


# Code to draw the shapes 
# Here we just drwa a square.

for side in range(4):
    pen.forward(100)
    pen.left(90)

# Each corner of the square is 100 and it turns 90 so you want the pen at 100 to the right and 100 up.
# Reminder, change numbers and hit run to test and see the directions the pen is moving and where is starting.
pen.penup()  #stops drwaing
pen.goto(100,100) # specfic location it will start from.
pen.pendown() # It will start drawing again.
pen.pencolor("red")
pen.fillcolor("green")  #This is the color you want to fill the triangle with.
pen.begin_fill() # This is the start of the fill color.
pen.left (120) # It will start drawing the triangle at 120 degrees to the left.
pen.forward(100) # do not forget that foward code is to move and draw in the direction of the pen or arrow.
pen.left(120)
pen.forward(100)
pen.end_fill() # This is the end of the fill color.
    
# Wait for user to close window
win.mainloop()

# Nathan Sparks
# 4 April 2026
# P4LAB1
# Using turtle to draw shapes with a "while" loop and "for" loop

# import turtle library
import turtle

# create the turtle window and drawing object
win = turtle.Screen ()
pen = turtle.Turtle ()

# Set turtle options
pen.pensize (5)
pen.pencolor ("blue")
pen.shape ("arrow")

# for loop to draw the square
for side in range (4) :
    pen.forward(200)
    pen.right (90)

# while loop to execute 3 times to draw a triangle
pen.pensize (5)
pen.pencolor ("green")
pen.shape ("arrow")

pen.fillcolor("green")
pen.begin_fill()

sides = 3

while sides > 0 :
    pen.forward(200)
    pen.left(120)
    sides = sides - 1

pen.end_fill()
    


# wait for user to close window
win.mainloop()
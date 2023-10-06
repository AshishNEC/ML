# draw Rectangle in Python Turtle
import turtle

t = turtle.Turtle()

l = int(input("Enter the length of the Rectangle: "))
w = int(input("Enter the width of the Rectangle: "))

# drawing first side
t.forward(l)  # Forward turtle by l units
t.left(90)  # Turn turtle by 90 degree

# drawing second side
t.forward(w)  # Forward turtle by w units
t.left(90)  # Turn turtle by 90 degree

# drawing third side
t.forward(l)  # Forward turtle by l units
t.left(90)  # Turn turtle by 90 degree

# drawing fourth side
t.forward(w)  # Forward turtle by w units
t.left(90)  # Turn turtle by 90 degree
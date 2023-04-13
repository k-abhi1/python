# Step 1 import and Set turtle's shape, color
import turtle
import time
turtle.shape("turtle")
turtle.color("red")

# Step 2 set turtle starting position
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.pensize(5)

# Step 3 Draw a heart shape
turtle.begin_fill()
turtle.left(140)
turtle.forward(224)
turtle.circle(-112, 200)
turtle.setheading(60)
turtle.circle(-112, 200)
turtle.forward(224)
turtle.end_fill()

# Step 4 Write I love you below heart shape
turtle.penup()
turtle.goto(-120, -180)
turtle.pendown()
turtle.write("I love you!", font=("Arial", 36, "normal"))

# Step 5 set turtle Background fancy colors
t = turtle.Turtle()
colors = ["purple","pink", "maroon", "magenta", "light slate blue",  "violet", "black"]

for color in colors:
    t.screen.bgcolor(color)
    time.sleep(1)

# step 6 Keep the window open until the user closes it
turtle.done()
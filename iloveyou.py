import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(3)
pen.color("red")
pen.width(4)

# Function to draw heart
def draw_heart():
    pen.begin_fill()
    pen.left(140)
    pen.forward(180)
    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)
    pen.forward(180)
    pen.end_fill()

# Move turtle to position
pen.penup()
pen.goto(0, -50)
pen.pendown()

# Draw heart
draw_heart()

# Write text
pen.penup()
pen.goto(0, 100)   # go to center of heart
pen.color("white")
pen.write("I Love You miss 🥰", align="center", font=("Arial", 24, "bold"))

turtle.done()
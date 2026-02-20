
# importing turtle library 
import turtle
#importing color library 
import colorsys

# creating the turtle 
t=turtle.Turtle()
#drowing speed 
t.speed(0)
#background color 
turtle.bgcolor("black")

#hue variable 
h = 0

#outer loop
for i in range (36):
    # inner loop used for hexagon
    for j in range (6):
        # color calculation
        c =colorsys.hsv_to_rgb(h,1,1)
        # for making smooth color change 
        t.color(c)
        # forward movement 
        t.forward(100)
        #rotating hexagon library 
        t.right(60)
        #hue increment for color changing
        h += 0.01
    # for adding circle too.
    # it is ouside from the inner loop    
    t.circle(60)
    #for rotate whole space
    t.right(10)
#syops turtle and keeps the window open
turtle.done()
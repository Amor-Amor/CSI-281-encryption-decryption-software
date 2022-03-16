import turtle

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Key Visualization")
draw = turtle.Turtle()

# Draw line to the left
# draw.forward(100)

# Draw a square
# for i in range(4):
#   draw.forward(50)
#   draw.right(90)

# Draw a star
# draw.right(75)
# draw.forward(100)
#
# for i in range(4):
#     draw.right(144)
#     draw.forward(100)

# Draw a hexagon
# num_sides = 6
# side_length = 70
# angle = 360.0 / num_sides
#
# for i in range(num_sides):
#     draw.forward(side_length)
#     draw.right(angle)

# Draw a key
# Draw bow
draw.circle(30)
# Draw blade
draw.right(90)
draw.forward(80)
# Draw first biting
draw.left(90)
draw.forward(30)
draw.right(180)
draw.forward(30)
# Draw rest of blade
draw.left(90)
draw.forward(20)
# Draw second biting
draw.left(90)
draw.forward(30)

turtle.done()
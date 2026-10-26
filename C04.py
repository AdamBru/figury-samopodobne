import turtle
import math

turtle.speed(0)
# Instant draw
turtle.tracer(0)

def draw(size, depth):
	roof_size = size / math.sqrt(2)

	if depth > 0:
		turtle.forward(size)
		turtle.left(45)
		draw(roof_size, depth - 1)
		turtle.right(90)
		turtle.forward(roof_size)
		draw(roof_size, depth - 1)
		turtle.right(90)
		turtle.forward(roof_size)
		turtle.right(45)
		turtle.forward(size)
		turtle.right(90)
		turtle.forward(size)
		turtle.right(90)


# set starting position
turtle.left(90)
turtle.penup()
turtle.goto(-100, -300)
turtle.pendown()

# Main starting point
draw(150, 12)

turtle.update()
turtle.done()
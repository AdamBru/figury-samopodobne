import turtle
turtle.speed(0)
# Instant draw
# turtle.tracer(0)

def draw(size, depth):
	if depth > 0:
		for angle in [45, 0, -45]:
			turtle.left(angle)
			turtle.forward(size)
			draw(size * multiplier, depth - 1)
			turtle.backward(size)
			turtle.right(angle)

# Move down on canvas
turtle.left(90)
turtle.penup()
turtle.goto(0, -300)
turtle.pendown()

# Parameters
multiplier = 0.666

# Main starting point
draw(192, 5)

turtle.update()
turtle.done()
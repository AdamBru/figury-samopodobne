import turtle
turtle.speed(0)
## Instant draw
# turtle.tracer(0)

def draw(size, depth):
	if (depth > 0):
		for count in range(3):
			turtle.forward(size)
			turtle.left(60)
			draw(size/2, depth-1)
			turtle.right(60 + 120)

turtle.left(180)
draw(128, 5)
turtle.done()
import turtle
turtle.speed(0)
## Instant draw
# turtle.tracer(0)

def draw(size, depth):
	if (depth > 0):
		for count in range(3):
			turtle.forward(size)
			turtle.right(180)
			draw(size/2, depth-1)
			turtle.left(180 + 120)

draw(256, 4)
turtle.done()
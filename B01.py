import turtle
turtle.speed(0)
turtle.tracer(0)

def draw(size, depth):
	if depth > 0:
		for count in range(4):
			turtle.forward(size)
			turtle.right(90)
			if count % 2 != 0:
				draw(size / 2, depth - 1)

draw(256, 5)
turtle.update()
turtle.done()
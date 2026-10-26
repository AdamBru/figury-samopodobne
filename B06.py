import turtle
turtle.speed(0)

def draw(size, depth):
	if depth > 0:
		for count in range(4):
			draw(size / 3, depth - 1)
			turtle.forward(size / 3)
			turtle.forward(size / 3 * 2)
			turtle.left(90)

draw(300, 4)
turtle.done()
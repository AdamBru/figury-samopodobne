import turtle
turtle.speed(0)

def draw(size, depth):
	if depth == 0:
		for count in range(3):
			turtle.forward(size)
			turtle.left(120)
	else:
		for count in range(3):
			draw(size / 3, depth - 1)
			turtle.forward(size / 3)
			turtle.forward(size / 3 * 2)
			turtle.left(120)

draw(300, 3)
turtle.done()
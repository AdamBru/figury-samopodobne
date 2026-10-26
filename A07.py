import turtle
turtle.speed(0)

def draw(size, depth):
	if depth > 0:
		for count in range(3):
			turtle.forward(size / 4)
			turtle.right(60)

			draw(size / 2, depth - 1)

			turtle.left(60)
			turtle.forward(3 * size / 4)
			turtle.left(120)

draw(243, 4)
turtle.done()
import turtle
turtle.speed(0)

def draw(size, depth):
	if depth > 0:
		for count in range(4):
			turtle.forward(size / 4)
			turtle.right(90)

			if count % 2 != 0:
				draw(size / 2, depth - 1)

			turtle.left(90)
			turtle.forward(3 * size / 4)
			turtle.left(90)

draw(128, 4)
turtle.done()
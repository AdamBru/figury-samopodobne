import turtle
turtle.speed(0)

def draw(size, depth):
	if depth > 0:
		for count in range(6):
			turtle.forward(size / 2)
			if count % 2 == 0:
				draw(size / 2, depth - 1)
			turtle.forward(size / 2)
			turtle.left(60)

draw(200, 4)
turtle.done()
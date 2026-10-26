import turtle
turtle.speed(0)
turtle.tracer(0)

def draw(size, depth):
	if depth > 0:
		for count in range(6):
			turtle.forward(size / 4)
			turtle.left(120)

			if count % 2 == 0:
				draw(size / 2, depth - 1)
			
			turtle.right(120)
			turtle.forward(3 * size / 4)
			turtle.right(60)
			
turtle.left(60)

draw(128, 3)
turtle.update()
turtle.done()
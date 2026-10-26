import turtle
turtle.speed(0)
turtle.tracer(0)

def draw(size, depth):
	if depth > 0:
		for count in range(4):
			turtle.left(90)
			turtle.forward(size)

			if count % 2 == 0:
				draw(size/2, depth-1)
			
			turtle.right(90 + 90)

turtle.left(90)

draw(128, 5)
turtle.update()
turtle.done()
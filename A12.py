import turtle
turtle.speed(0)
turtle.tracer(0)

def draw(size, depth):
	if depth == 0:
		for i in range(3):
			turtle.forward(size)
			turtle.left(120)
	else:
		for i in range(3):
			draw(size / 3, depth - 1)
			turtle.forward(size / 3)
			
			draw(size / 3, depth - 1)
			turtle.forward(size / 3 * 2)
			
			turtle.left(120)


size = 415

turtle.penup()
turtle.goto(size / -2, size / -2)
turtle.pendown()

draw(size, 3)
turtle.update()
turtle.done()
import turtle

turtle.speed(0)
# Instant draw
turtle.tracer(0)

def draw(size, depth):
	if depth > 0:
		draw(size / 3, depth - 1)

		for angle in [90, 0, -90, 180]:
			turtle.left(angle)
			turtle.forward(size)

			draw(size / 3, depth - 1)

			turtle.backward(size)
			turtle.left(-angle)


# set starting position
turtle.left(90)

draw(192, 5)

turtle.update()
turtle.done()
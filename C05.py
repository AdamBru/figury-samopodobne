## SIERPINSKI CARPET
import turtle

turtle.speed(0)
turtle.delay(0)
# Instant draw
# turtle.tracer(0)

def draw(size, depth):
	if depth == 0:
		for count in range(4):
			turtle.forward(size)
			turtle.left(90)
	else:
		for row in range(3):
			for col in range(3):
				if not(row == 1 and col == 1):
					draw(size / 3, depth - 1)
				
				turtle.forward(size / 3)

			turtle.backward(size)
			turtle.left(90)
			turtle.forward(size / 3)
			turtle.right(90)

		turtle.left(90)
		turtle.backward(size)
		turtle.right(90)

# set starting position
turtle.penup()
turtle.goto(-300, -300)
turtle.pendown()

draw(400, 4)
turtle.update()
turtle.done()
import turtle
turtle.speed(0)
# Instant draw
turtle.tracer(0)

def draw(size, depth):
	turtle.color('green')

	if depth > 0:
		turtle.forward(size)
		turtle.left(45)
		
		draw(size * multiplier, depth - 1)

		turtle.right(90)

		draw(size * multiplier, depth - 1)

		turtle.left(45)

		turtle.backward(size)
		

# Move down on canvas
turtle.left(90)
turtle.penup()
turtle.goto(0, -300)
turtle.pendown()

# Parameters
multiplier = 0.666
size = 192

# Main starting point
draw(size, 10)

# Paint the trunk brown
turtle.color('brown')
turtle.forward(size)
turtle.backward(size)

turtle.update()
turtle.done()
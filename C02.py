import turtle
turtle.speed(0)

def draw(size):
	if size > 0:
		turtle.forward(size)
		turtle.left(144)
		draw(size - 15)


turtle.penup()
turtle.goto(-220, 0)
turtle.pendown()

draw(450)
turtle.done()
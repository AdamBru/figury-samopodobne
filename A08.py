import turtle
turtle.speed(0)

def draw(size):
	if size > 0:
		turtle.forward(size)
		turtle.left(120)
		draw(size - 10)


turtle.penup()
turtle.goto(-220, -200)
turtle.pendown()

draw(450)
turtle.done()
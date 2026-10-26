import turtle
turtle.speed(0)
# turtle.tracer(0)

def draw(size):
	if size > 1:
		turtle.forward(size)
		turtle.left(95)
		draw(size - 3)

turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()

draw(400)
turtle.update()
turtle.done()
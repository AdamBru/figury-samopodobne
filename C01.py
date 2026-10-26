import turtle
turtle.speed(0)
# turtle.tracer(0)

def draw(size):
	if size > 1:
		turtle.forward(size)
		turtle.right(117)
		draw(size - 3)

turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()

draw(512)
turtle.update()
turtle.done()
import turtle
turtle.speed(0)

def draw(size):
	if size > 0:
		turtle.left(60)
		turtle.forward(size)
		draw(size - 5)
			

draw(192)
turtle.done()
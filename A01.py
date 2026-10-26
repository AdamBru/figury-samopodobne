import turtle

def draw(size, depth):
	if (depth > 0):
		# Recursive
		for count in range(4):
			turtle.forward(size)
			draw(size/2, depth-1)
			turtle.right(90)

		# Non-Recursive
		# for count in range(4):
		# 	turtle.forward(size)
		# 	for count in range(4):
		# 		turtle.forward(size / 2)
		# 		for count in range(4):
		# 			turtle.forward(size / 4)
		# 			for count in range(4):
		# 				turtle.forward(size / 8)
		# 				turtle.right(90)
		# 			turtle.right(90)
		# 		turtle.right(90)
		# 	turtle.right(90)

# Instant draw
turtle.tracer(0)

turtle.speed(0)
# (size, depth)
draw(256, 4)
turtle.done()
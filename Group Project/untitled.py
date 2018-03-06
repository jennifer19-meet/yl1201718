import turtle
turtle.ht()
turtle.setup( width = 1500, height = 1500, startx = None, starty = None)
turtle.tracer(0)
turtle.pu()
turtle.goto(-650,400)
for rows in range(-4, 3):

		turtle.forward(1000)
		turtle.right(90)
		turtle.pu()
		turtle.forward(50)
		turtle.right(90)
		turtle.pd()
		turtle.forward(1000)
		turtle.left(90)
		turtle.pu()
		turtle.forward(50)
		turtle.left(90)
		turtle.pd()

turtle.left(90)
for collumns in range (-4,3):
	
	turtle.forward(1000)
	turtle.right(90)
	turtle.pu()
	turtle.forward(50)
	turtle.right(90)
	turtle.pd()
	turtle.forward(1000)
	turtle.left(90)
	turtle.pu()
	turtle.forward(50)
	turtle.left(90)
	turtle.pd()

turtle.mainloop()
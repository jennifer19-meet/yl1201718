#Exercise One:
import turtle
turtle.pencolor("red")
turtle.penup()
turtle.goto(0,0)
turtle.pendown()

def star(times):
	for i in range(times):
		turtle.forward(100)
		turtle.right(144)
	
star(5)
turtle.mainloop()




#Exercise Two:

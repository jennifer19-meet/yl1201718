#Exercise One:
""""
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
"""



#Exercise Two:
'''
import turtle
turtle.register_shape("weird_shape", ((0,10),(10,10),(10,0),(5,-5), (0,0)))
turtle.shape("weird_shape")
turtle.goto (0,50)
turtle.goto(50,50)
turtle.goto(50,0)
turtle.goto(25,-25)
turtle.goto(0,0)
turtle.mainloop()
'''

'''
#Exercise Three:
import turtle
turtle.addshape("1sntGUp.gif")
turtle.shape("1sntGUp.gif")
number=0
def coolshape (times):
	for i in range (times):
		turtle.home()
		turtle.right(i)
		turtle.speed(5000)
		turtle.forward(200)
		turtle.right(40)
		turtle.forward(100)
		turtle.right(90)
		turtle.forward(50)
		
coolshape(360)
turtle.mainloop()
'''

#Exercise 4:

import turtle
x=0
for i in range (360):
	turtle.forward(100)
	turtle.right(40)
	turtle.forward(60)
	turtle.right(90)
	turtle.forward(30)
	turtle.pu()
	turtle.home()
	turtle.pd()
	turtle.right(x+i)
	turtle.speed(3000)

turtle.mainloop()
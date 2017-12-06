from turtle import *
import random
import math
#screen.screensize()
class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

def checkCollision(ball1, ball2):
	global y1
	global y2
	global x1
	global x2
	global r1
	global r2

	x1 = ball1.xcor()
	y1 = ball1.ycor()

	x2 = ball2.xcor()
	y2 = ball2.ycor()

	r1 = ball1.radius
	r2 = ball2.radius
	
	global D
	D = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
	
	if (D < r1 + r2):
		ball1.color("black")
		ball2.color("green")
ball1 = Ball(15, "pink", 1)
ball2 = Ball(10, "red", 1)
list9 = [ball1,ball2]
ball1.backward(20)
ball2.forward(20)

checkCollision(ball1, ball2)

ball1.backward(-11)
ball2.forward(-11)

checkCollision(ball1, ball2)
def cooliooo():
	if (D < r1 + r2):
		print("Collision")
		if r1 >r2:
			y = random.randint(-70,700) 
			x = random.randint(-70,700)
			ball2.goto(x,y)
		else:
			y = random.randint(-70,700) 
			x = random.randint(-70,700)
			ball1.goto(x,y)


cooliooo()

mainloop()

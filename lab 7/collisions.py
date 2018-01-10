"""

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
"""
from turtle import *
import random
import math

rec_count = 0

class Rectangle (Turtle):
	def __init__(self, color, width, height, speed):
		global rec_count

		Turtle.__init__(self)
		rec_count += 1

		register_shape("my_rec" + str(rec_count), ((width,0), (width,height), (0,height), (0,0)))
		self.shape("my_rec" + str(rec_count))
		self.fillcolor(color)
		self.speed(speed)
		self.width = width
		self.height = height
	def top (self):
		return self.ycor() + self.height/2
	def bottom (self):
		return self.ycor() - self.height/2
	def right (self):
		return self.xcor() + self.width/2
	def left (self):
		return self.xcor() - self.width/2

def check_collision (A, B):
	if(A.top() >= B.bottom() and A.right() >= B.left() and A.bottom() <= B.top() and A.left() <= B.right()):
		return True


rectangle1 = Rectangle("red",10,30,4)
rectangle2 = Rectangle("blue", 70,50,3) 
rectangle2.goto (100,60)
rectangle1.goto (100,60)
print(check_collision (rectangle1, rectangle2))

mainloop()

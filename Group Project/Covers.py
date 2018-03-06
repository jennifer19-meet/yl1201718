from turtle import *

class Square2(Turtle):
	def __init__(self,size, x, y, color):
		Turtle.__init__(self)
		self.pu()
		self.shape("square")
		self.size = size
		self.shapesize(size)
		self.x = x
		self.y = y
		self.color(color)
		self.goto(x,y)
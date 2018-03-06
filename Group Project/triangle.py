from turtle import *

class Triangle(Turtle):
	def __init__(self, x, y , color):
		Turtle.__init__(self)
		self.pu()
		self.x =x
		self.y = y
		self.color(color)
		self.goto(x,y)
		
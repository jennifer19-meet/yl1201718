from turtle import *

class Tturtle(Turtle):
	def __init__(self, x, y, color):
		Turtle.__init__(self)
		self.pu()
		self.shape("turtle")
		self.x = x
		self.y = y
		self.color(color)
		self.goto(x,y)
	
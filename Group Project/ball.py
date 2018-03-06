from turtle import *

class Ball(Turtle):
	def __init__(self, x, y ,  color):
		Turtle.__init__(self)
		self.pu()
		self.shape("circle")
		# radius = r
		# self.shapesize(r/10)
		# self.r = radius

		self.x =x
		self.y = y
		self.color(color)
		self.goto(x,y)

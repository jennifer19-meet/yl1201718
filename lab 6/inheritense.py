#Exercise One:
"""


from turtle import *
import random
colormode(255)
class Square(Turtle):
	def __init__ (self,size,color):
		Turtle.__init__(self)
		self.shapesize (size)
		self.shape("square")
		self.color(color)
		
	def  random_color (self):
		r = random.randint(0, 257)
		g = random.randint(0, 257)
		b = random.randint(0, 257)
		self.color ((r,g,b))

square1 = Square(2,"red")
square1.random_color()
mainloop()

"""

#Exercise Two:
from turtle import Turtle
turtle.registershape(hex ())
class Hexagon(object):
	def __init__ (self,size,color):
		self.shapesize(size)
		self.color(color)
		self.shape()
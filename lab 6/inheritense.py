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
from turtle import *

'''
begin_poly()
def hexi():
	for i in range (6):
		pu()
		hideturtle()
		forward(25)
		right(60)
		speed(3000)

hexi()
end_poly()


p = get_poly()
register_shape("Hexagon", p)
class Hexagon(Turtle):
	def __init__ (self, size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.color("violet")
		self.shape("Hexagon")
'''
#hi = Hexagon(0.5)

#Extras:
from turtle import *
class Poly(Turtle):
	def __init__ (self,line):
		Turtle.__init__(self)
		
		begin_poly()	
		for i in range (line):
			pu()
			hideturtle()
			speed(30000)
			forward(50)
			right (360/line)
		end_poly()
		r = get_poly()
		register_shape("polygonz", r)
		self.shape("polygonz")
dan = Poly (7)

mainloop()
 #Exercise 3:
 
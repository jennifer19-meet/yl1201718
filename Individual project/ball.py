from turtle import *

class Ball(Turtle):
	def __init__(self, x, y ,dx, dy, r, color):
		Turtle.__init__(self)
		self.pu()
		self.shape("circle")
		radius = r
		self.shapesize(r/10)
		self.r = radius
		self.dx = dx
		self.dy = dy
		self.x =x
		self.y = y
		self.color(color)
		self.goto(x,y)
	def move (self,screen_width,screen_height):
		current_x = self.xcor()
		new_x = current_x+ self.dx
		current_y = self.ycor()
		new_y = current_y+ self.dy 
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		top_side_ball = new_y + self.r
		bottom_side_ball = new_y - self.r
		self.x = new_x
		self.y = new_y
		self.goto(new_x, new_y)
		if right_side_ball>screen_width or left_side_ball<-screen_width:
			self.dx = self.dx*-1
		if top_side_ball>screen_height or bottom_side_ball <-screen_height:
			self.dy= self.dy*-1




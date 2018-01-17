import random
import time
import turtle
from ball import Ball 

turtle.tracer(0)
turtle.colormode(255)
BALLS=[]
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5.
MAXIMUM_BALL_DY = 5
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

MY_BALL= Ball(3,4,90,50,30,"blue")

for i in range (NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(0>MINIMUM_BALL_DX, 0<MAXIMUM_BALL_DX)
	dy = random.randint(0>MINIMUM_BALL_DY, 0<MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
	ball2 = Ball(x,y, dx,dy,radius,color)
	BALLS.append(ball2)
def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH, SCREEN_HEIGHT)
move_all_balls()

def collision(ball_a,ball_b):
	if ball_a==ball_b:
		return False
	right_a = ball_a.x + ball_a.r
	left_a = ball_a.x - ball_a.r
	top_a = ball_a.y + ball_a.r
	bottom_a = ball_a.y - ball_a.r
	right_b = ball_b.x + ball_b.r
	left_b = ball_b.x - ball_b.r
	top_b = ball_b.y + ball_b.r
	bottom_b = ball_b.y - ball_b.r
	if right_a>left_b and left_a :
		
turtle.update()
turtle.mainloop()
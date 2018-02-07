import random
import time
import turtle
from ball import Ball 
import math

turtle.tracer(0)
turtle.colormode(255)
BALLS=[]
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 60
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 2
MINIMUM_BALL_DY = -5.
MAXIMUM_BALL_DY = 2
turtle.hideturtle()
RUNNING = True
SLEEP = 0.0077
canvas = turtle.getcanvas()
SCREEN_WIDTH = canvas.winfo_width()/2
SCREEN_HEIGHT = canvas.winfo_height()/2
#i have isuues with screen height and width
#worked with int()
MY_BALL= Ball(3,4,0,0,35,"blue")

for i in range (NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	while dx == 0:
		dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	while dy ==0:
		dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
	ball2 = Ball(x,y, dx,dy,radius,color)
	BALLS.append(ball2)
def move_all_balls():
	for i in BALLS:
		i.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collision(ball_a,ball_b):
	if ball_a==ball_b:
		return False	
	sumoftwo = ball_a.r +ball_b.r
	distancebetweentwo = math.sqrt((math.pow(ball_a.x - ball_b.x, 2)) + (math.pow(ball_a.y - ball_b.y, 2)))

	if sumoftwo>= distancebetweentwo + 10:
	
		return True
	else:
		return False

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collision(ball_a, ball_b) == True:
				
				r_a = ball_a.r
				r_b = ball_b.r

				x2 = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y2 = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				x_speed2 = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				y_speed2 = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				while x_speed2 == 0:
					x_speed2 = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				while y_speed2 ==0:
					y_speed2 = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				radius2 = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				color2 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

				if r_a>r_b :
					ball_b.r = radius2
					ball_b.shapesize(ball_b.r/10)
					ball_b.color = color2
					ball_b.goto(x2,y2)
					ball_b.dx = x_speed2
					ball_b.dy = y_speed2
					ball_a.r = ball_a.r +1
					ball_a.shapesize(ball_a.r/10)
				else :
					ball_a.r = radius2
					ball_a.shapesize(ball_a.r/10)
					ball_a.color = color2
					ball_a.goto(x2,y2)
					ball_a.dx =x_speed2
					ball_a.dy = y_speed2
					ball_b.r = ball_b.r + 1
					ball_b.shapesize(ball_b.r/10)


def check_myball_collision():
	for i in range (len(BALLS)):
		if collision(MY_BALL,BALLS[i]):

			r_of_meee = MY_BALL.r
			r_of_themm = BALLS[i].r
			if r_of_themm> r_of_meee:
				return False
			else:
				x3 = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y3 = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)				
				x_speed3 = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				y_speed3 = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				while x_speed3 == 0:
					x_speed3 = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				while y_speed3 ==0:
					y_speed3 = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				radius3 = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				color3 = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
				BALLS[i].r = radius3
				BALLS[i].shapesize(BALLS[i].r/10)
				BALLS[i].color = color3
				BALLS[i].goto(x3,y3)
				BALLS[i].dx =x_speed3
				BALLS[i].dy =y_speed3
				MY_BALL.r = MY_BALL.r +1 
				MY_BALL.shapesize(MY_BALL.r/10)
	return True
def movearound(event):
	MY_BALL.goto((event.x - SCREEN_WIDTH),(SCREEN_HEIGHT - event.y))
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while RUNNING is True:
	if SCREEN_WIDTH != canvas.winfo_width()/2:
		SCREEN_WIDTH = canvas.winfo_width()/2
	if SCREEN_HEIGHT  != canvas.winfo_height()/2:
		SCREEN_HEIGHT =canvas.winfo_height()/2
	move_all_balls()
	check_all_balls_collision()
	MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)

	RUNNING= check_myball_collision()

	turtle.getscreen().update()
	time.sleep(SLEEP)





turtle.mainloop()
import turtle
import random
import time 
from ball import Ball
from square import Square
from arrow import Arrow
from triangle import Triangle
from Turtle import Tturtle
from Covers import Square2

top_covers_x_y=[]
x_y = []
colors = ["blue","red","pink","green"]
shapes = [Square,Ball, Arrow, Tturtle,Triangle]


running = True

turtle.bgcolor("black")
spacing = 110
max_height = 3
min_height = -2
max_width = 4
min_width = -4
turtle.ht()
turtle.tracer (0)
turtle.setup( width = 1500, height = 1500, startx = None, starty = None)


for y in range(min_height, max_height):
	for x in range(min_width, max_width):
		cover = Square2(4,x,y,"white")
		cover.goto(x * spacing, y * spacing)
i=0
while i < 40:
	randcoverx = random.randint (min_width,3)
	randcovery = random.randint (min_height,2)
	if (randcoverx,randcovery) not in x_y:
		x_y.append((randcoverx,randcovery))
		i+=1

print(x_y)
print(len(x_y))
hi = 0
xandypoint = 0
for g in range (4):

	hii = 0
	for t in range(5):
		
		shapem = shapes[hii](x_y[xandypoint][0]*110,x_y[xandypoint][1]*110, colors[hi])
		xandypoint+=1
		shapem2 = shapes[hii](x_y[xandypoint][0]*110,x_y[xandypoint][1]*110, colors[hi])
		hii +=1
		xandypoint+=1
		
	hi+=1

for y in range(min_height, max_height):
	for x in range(min_width, max_width):
		cover1 = Square2(4,x,y,"white")
		cover1.goto(x * spacing, y * spacing)
		top_covers_x_y.append((cover1.xcor(),cover1.ycor()))
		hi+=1
#turtle.onscreenclick() if the other one doesnt work
def get_mouse_click_cor(x, y):
    turtle.onscreenclick(None)
    print(x, y)

def clicked():
	for i in range (len(top_covers_x_y)):
		if turtle.onscreenclick(get_mouse_click_cor) ==top_covers_x_y[i]:
			top_covers_x_y[i].ht()
while running == True:
	turtle.onscreenclick(get_mouse_click_cor)	
	turtle.listen()







turtle.update()


turtle.mainloop()
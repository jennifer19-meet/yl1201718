import turtle
import time
import random

user_inputs = turtle.clone()
clock = turtle.clone()
clock.ht()
user_inputs.ht()
user_inputs.pu()
turtle.ht()
turtle.setup( width = 1500, height = 1500, startx = None, starty = None)
turtle.tracer(0)
turtle.pu()
running = True

randx_randy =[]
randx_randnum =[]
randy_randnum =[]
#this list will help for the 9 boxes
box_help = []
box_1 = []
box_2 = []
box_3 = []
box_4 = []
box_5 = []
box_6 = []
box_7 = []
box_8 = []
box_9 = []
boxes=[]
numbers_possible = [1,2,3,4,5,6,7,8,9]
boxes.append(box_1)	
boxes.append(box_2)	
boxes.append(box_3)	
boxes.append(box_4)	
boxes.append(box_5)	
boxes.append(box_6)	
boxes.append(box_7)	
boxes.append(box_8)	
boxes.append(box_9)	

x=-200
y=-200
spacing = 44.5 

for rows in range(-5, 5):
	turtle.goto(x,y)
	turtle.pd()
	turtle.forward(400)
	y=y+spacing
	turtle.pu()
	turtle.color("grey")

x=-200
y=-200
		
turtle.color("black")
turtle.left(90)
for collumns in range (-5,5):
	turtle.goto(x,y)
	turtle.pd()
	turtle.forward(400)
	x=x+spacing
	turtle.pu()
	turtle.color("grey")

x=-200
y=-200
turtle.color("black")
turtle.right(90)
for darker_rows in range (3):
	
	y=y+spacing*3
	turtle.goto(x,y)
	turtle.pd()
	turtle.forward(400)
	turtle.pu()
x=-200
y=-200

turtle.left(90)
for darker_collumns in range (3):
	
	x=x+spacing*3
	turtle.goto(x,y)
	turtle.pd()
	turtle.forward(400)
	turtle.pu()


# def game_setup():
number_of_numbers= random.randint(32,36)
for i in range (number_of_numbers):
	x=-200
	y=-200
	rand_number= random.randint(1,9)
	rand_collumn = random.randint(1,9)
	x= x+(rand_collumn-1)*spacing+0.25*spacing
	
	
	rand_row = random.randint(1,9)
	y=y+(rand_row-1)*spacing+0.25*spacing
	if (x,y) not in randx_randy and (x,rand_number) not in randx_randnum and (y,rand_number) not in randy_randnum:
		randx_randy.append((x,y))
		randx_randnum.append((x,rand_number))
		randy_randnum.append((y,rand_number))
		box_help.append(x)
		box_help.append(y)
		box_help.append(rand_number)
		turtle.goto(x,y)
		turtle.write (str(rand_number), font=("Papyrus", 20, "normal"))
		if x>=-188.875 and x<=-99.875 and y>=-188.875 and y<=-99.875:
			box_1.append(x)
			box_1.append(y)
			box_1.append(rand_number)
			boxes.remove(box_1)
			boxes.append(box_1)
		if x>=-55.375 and x<=33.625 and y>=-188.875 and y<=-99.875:
			box_2.append(x)
			box_2.append(y)
			box_2.append(rand_number)
			boxes.remove(box_2)
			boxes.append(box_2)
		if x>=78.125 and x<=167.125 and y>=-188.875 and y<=-99.875:
			box_3.append(x)
			box_3.append(y)
			box_3.append(rand_number)
			boxes.remove(box_3)
			boxes.append(box_3)
		if x>=78.125 and x<=167.125 and y>=-55.375 and y<=33.625:
			box_4.append(x)
			box_4.append(y)
			box_4.append(rand_number)
			boxes.remove(box_4)
			boxes.append(box_4)
		if x>=-55.375 and x<=33.625 and y>=-55.375 and y<=33.625:
			box_5.append(x)
			box_5.append(y)
			box_5.append(rand_number)
			boxes.remove(box_5)
			boxes.append(box_5)
		if x>=-188.875 and x<=-99.875 and y>=-55.375 and y<=33.625:
			box_1.append(x)
			box_1.append(y)
			box_6.append(rand_number)
			boxes.remove(box_6)
			boxes.append(box_6)
		if x>=-188.875 and x<=-99.875 and y>=78.125 and y<=167.125:
			box_7.append(x)
			box_7.append(y)
			box_7.append(rand_number)
			boxes.remove(box_7)
			boxes.append(box_7)
		if x>=-55.375 and x<=33.625 and y>=78.125 and y<=167.125:
			box_8.append(x)
			box_8.append(y)
			box_8.append(rand_number)
			boxes.remove(box_8)
			boxes.append(box_8)
		if x>=78.125 and x<=167.125 and y>=78.125 and y<=167.125:
			box_9.append(x)
			box_9.append(y)
			box_9.append(rand_number)
			boxes.remove(box_9)
			boxes.append(box_9)
		for j in range (len(boxes)):
			if (int(len(boxes[j]))+1)%3 == 0:
				# for p in range ((int(len(boxes[j]))+1)/3):
					print(int(len(boxes[j]))/3)
					print((int(len(boxes[j]))+1)%3)
					# while boxes[j].count(1)>1 or boxes[j].count(2)>1 or boxes[j].count(3)>1 or boxes[j].count(4)>1 or boxes[j].count(5)>1 or boxes[j].count(6)>1 or boxes[j].count(7)>1 or boxes[j].count(8)>1 or boxes[j].count(9)>1 :
					# 	if boxes[j].count(1)>1:
						
							
					# 		boxes[j].pop(-1)
							
					# 		rand_number= random.randint(1,9)
					# 		boxes[j].append(rand_number)
					# 	if boxes[j].count(2)>1:
					# 		boxes[j].pop(-1)
							
					# 		rand_number= random.randint(1,9)
					# 		boxes[j].append(rand_number)
							
					# 	if boxes[j].count(3)>1:
							
					# 		boxes[j].pop(-1)
							
					# 		rand_number= random.randint(1,9)
					# 		boxes[j].append(rand_number)
					# 	if boxes[j].count(4)>1:
					# 		boxes[j].pop(-1)
							
					# 		rand_number= random.randint(1,9)
					# 		boxes[j].append(rand_number)
					# 	if boxes[j].count(5)>1:
							
					# 		boxes[j].pop(-1)
							
					# 		rand_number= random.randint(1,9)
					# 		boxes[j].append(rand_number)
					# 	if boxes[j].count(6)>1:
							
					# 		boxes[j].pop(-1)
							
					# 		rand_number= random.randint(1,9)
					# 		boxes[j].append(rand_number)
					# 	if boxes[j].count(7)>1:
							
					# 		boxes[j].pop(-1)
							
					# 		rand_number= random.randint(1,9)
					# 		boxes[j].append(rand_number)
					# 	if boxes[j].count(8)>1:
							
					# 		boxes[j].pop(-1)
							
					# 		rand_number= random.randint(1,9)
					# 		boxes[j].append(rand_number)
					# 	if boxes[j].count(9)>1:
					# 		boxes[j].pop(-1)
							
					# 		rand_number= random.randint(1,9)
					# 		boxes[j].append(rand_number)
			# else:
			# 	pass

	else:
		while (x,y) in randx_randy or (x,rand_number) in randx_randnum or (y,rand_number) in randy_randnum:
			x=-200
			y=-200
			rand_number= random.randint(1,9)
			rand_collumn = random.randint(1,9)
			x= x+(rand_collumn-1)*spacing+0.25*spacing
			
			
			rand_row = random.randint(1,9)
			y=y+(rand_row-1)*spacing+0.25*spacing
		randx_randy.append((x,y))
		randx_randnum.append((x,rand_number))
		randy_randnum.append((y,rand_number))
		box_help.append(x)
		box_help.append(y)
		box_help.append(rand_number)
		turtle.goto(x,y)
		turtle.write (str(rand_number), font=("Papyrus", 20, "normal"))
		if x>=-188.875 and x<=-99.875 and y>=-188.875 and y<=-99.875:
			box_1.append(x)
			box_1.append(y)
			box_1.append(rand_number)
			boxes.remove(box_1)
			boxes.append(box_1)
		if x>=-55.375 and x<=33.625 and y>=-188.875 and y<=-99.875:
			box_2.append(x)
			box_2.append(y)
			box_2.append(rand_number)
			boxes.remove(box_2)
			boxes.append(box_2)
		if x>=78.125 and x<=167.125 and y>=-188.875 and y<=-99.875:
			box_3.append(x)
			box_3.append(y)
			box_3.append(rand_number)
			boxes.remove(box_3)
			boxes.append(box_3)
		if x>=78.125 and x<=167.125 and y>=-55.375 and y<=33.625:
			box_4.append(x)
			box_4.append(y)
			box_4.append(rand_number)
			boxes.remove(box_4)
			boxes.append(box_4)
		if x>=-55.375 and x<=33.625 and y>=-55.375 and y<=33.625:
			box_5.append(x)
			box_5.append(y)
			box_5.append(rand_number)
			boxes.remove(box_5)
			boxes.append(box_5)
		if x>=-188.875 and x<=-99.875 and y>=-55.375 and y<=33.625:
			box_1.append(x)
			box_1.append(y)
			box_6.append(rand_number)
			boxes.remove(box_6)
			boxes.append(box_6)
		if x>=-188.875 and x<=-99.875 and y>=78.125 and y<=167.125:
			box_7.append(x)
			box_7.append(y)
			box_7.append(rand_number)
			boxes.remove(box_7)
			boxes.append(box_7)
		if x>=-55.375 and x<=33.625 and y>=78.125 and y<=167.125:
			box_8.append(x)
			box_8.append(y)
			box_8.append(rand_number)
			boxes.remove(box_8)
			boxes.append(box_8)
		if x>=78.125 and x<=167.125 and y>=78.125 and y<=167.125:
			box_9.append(x)
			box_9.append(y)
			box_9.append(rand_number)
			boxes.remove(box_9)
			boxes.append(box_9)
		for j in range (len(boxes)):
			# if ((int(len(boxes[j]))+1)/3):
				print((int(len(boxes[j]))+1)/3)
				print((int(len(boxes[j]))+1)%3)
				# for p in range ((len(boxes[j])+1)/3):		
				# 	while boxes[j].count(1)>1 or boxes[j].count(2)>1 or boxes[j].count(3)>1 or boxes[j].count(4)>1 or boxes[j].count(5)>1 or boxes[j].count(6)>1 or boxes[j].count(7)>1 or boxes[j].count(8)>1 or boxes[j].count(9)>1 :
				# 		if boxes[j].count(1)>1:
						
							
				# 			boxes[j].pop(-1)
							
				# 			rand_number= random.randint(1,9)
				# 			boxes[j].append(rand_number)
				# 		if boxes[j].count(2)>1:
				# 			boxes[j].pop(-1)
							
				# 			rand_number= random.randint(1,9)
				# 			boxes[j].append(rand_number)
							
				# 		if boxes[j].count(3)>1:
							
				# 			boxes[j].pop(-1)
							
				# 			rand_number= random.randint(1,9)
				# 			boxes[j].append(rand_number)
				# 		if boxes[j].count(4)>1:
				# 			boxes[j].pop(-1)
							
				# 			rand_number= random.randint(1,9)
				# 			boxes[j].append(rand_number)
				# 		if boxes[j].count(5)>1:
							
				# 			boxes[j].pop(-1)
							
				# 			rand_number= random.randint(1,9)
				# 			boxes[j].append(rand_number)
				# 		if boxes[j].count(6)>1:
							
				# 			boxes[j].pop(-1)
							
				# 			rand_number= random.randint(1,9)
				# 			boxes[j].append(rand_number)
				# 		if boxes[j].count(7)>1:
							
				# 			boxes[j].pop(-1)
							
				# 			rand_number= random.randint(1,9)
				# 			boxes[j].append(rand_number)
				# 		if boxes[j].count(8)>1:
							
				# 			boxes[j].pop(-1)
							
				# 			rand_number= random.randint(1,9)
				# 			boxes[j].append(rand_number)
				# 		if boxes[j].count(9)>1:
				# 			boxes[j].pop(-1)
							
				# 			rand_number= random.randint(1,9)
				# 			boxes[j].append(rand_number)
			# else:
			# 	pass
print(boxes)
# print (randx_randnum)
# print(randy_randnum)

			
	


	












# game_setup()

# print(box_1)
# print(box_2)
# print(box_3)
# print(box_4)
# print(box_5)
# print(box_6)
# print(box_7)
# print(box_8)
# print(box_9)




while running == True:
	
	x=-200
	y=-200
	collumn_to_put = int(input("what collumn?"))
	x= x+(collumn_to_put-1)*spacing+0.25*spacing
	row_to_put = int(input("what row?"))
	y=y+(row_to_put-1)*spacing+0.25*spacing
	number_to_put = int(input("what number?"))

	if number_to_put> numbers_possible[-1]:
		number_to_put = int(input("The number you just entered is too big.What other number?(Between 1 and 9)"))
	if number_to_put< numbers_possible[0]:
		number_to_put = int(input("The number you just entered is too small.What other number?(Between 1 and 9)"))
	user_inputs.goto(x,y)
	user_inputs.write (str(number_to_put), font=("Papyrus", 20, "normal"))
	turtle.getscreen().update()
turtle.mainloop()
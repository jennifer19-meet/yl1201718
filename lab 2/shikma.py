#Exercise 1
'''

def shira():
	shikma = ["a", "o", "j", "k", "p"]
	hiii = [shikma[0], shikma[-1]]
	return(hiii)

print (shira())
'''
#Exercise 2
a= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in range (11):
	if a [0+i]<5:
		print(a[0+i])



#extras:
#A:
a= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
for i in range (11):
	if a [0+i]<5:
			b.append(a[0+i])
print(b)


#B
a= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
number = int(input('Type a number!!'))
for i in range (11):
	if a [0+i]<number:
			b.append(a[0+i])
print(b)



#Exercise 3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
for i in range (89):
	if a.count(0+i)>0 and b.count(0+i)>0:
			c.append(i)
print(c)



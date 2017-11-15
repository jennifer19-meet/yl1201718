#Problem 1
"""
class Animal(object):
	def __init__(self,sound,name,age,favourite_color):
			self.sound = sound
			self.name = name
			self.age = age
			self.favourite_color = favourite_color
	def eat(self,food):
		print("Yummmmmyy!!" + self.name + " is eating " + food)
	def description(self):
		print (self.name + " is " + self.age +" years old and loves the color " + self.favourite_color)
Cat = Animal("meow","Mo", "5", "red")
Cat.eat ("tomato")
Cat.description()
 """
 #Problem 2:
 '''
 class Animal(object):
	def __init__(self,sound,name,age,favourite_color):
			self.sound = sound
			self.name = name
			self.age = age
			self.favourite_color = favourite_color
	def eat(self,food):
		print("Yummmmmyy!!" + self.name + " is eating " + food)
	def description(self):
		print (self.name + " is " + self.age +" years old and loves the color " + self.favourite_color)
	def make_sound(self, favourite_sound, number):
		for i in range (number):
			print ((favourite_sound + " ")*i)
Cat = Animal("meow","Mo", "5", "red")
Cat.make_sound ("perrnaw", 8)
#Extra
'''


#Problem 3
'''
class Person(object):
	def __init__(self, name, age, city, gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def eat(self, favourite_breakfast):
		print(self.name + " "+ "is eating" +" "+favourite_breakfast +"!")
	def sport(self, favourite_sport):
		print(self.name + " "+"is playing"+" "+ favourite_sport)
Human= Person("jeff","27","rome","male")
Human.eat ("pancakes")
Human.sport ("basketball")
'''

#Extras
class Song(object):
	def __init__ (self, lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self, lyrics):
			print(lyrics)
flower_song = Song(["Roses are red",
				"Violets are blue",
				 			 "I wrote this poem for you"])
flower_song.sing_me_a_song()
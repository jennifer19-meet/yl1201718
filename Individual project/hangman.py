import turtle
import random
import time
turtle.ht()
turtle.tracer(0)
turtle.setup( width = 1500, height = 1500, startx = None, starty = None)
turtle.pu()
title = turtle.clone()
title.ht()
title.goto(400,300)
trys_left = 10

title.write("Trys Left = "+ str(trys_left) ,move= False, font=("Papyrus", 20, "normal"))

words = [ "about", "above", "across", "act", "active", "activity", "add", "afraid", "after", "again", "age", "ago", "agree", "air", "all", "alone", "along", "already", "always", "amount","angry", "another","answer", "anyone", "anything", "anytime", "appear", "apple","area", "arm", "army", "around", "arrive", "art", "attack", "aunt", "autumn", "away","baby", "back", "bad", "bag", "ball", "bank", "base", "basket", "bath","bean", "bear", "beautiful", "bed", "bedroom", "beer", "behave", "before", "begin", "behind", "bell", "below", "besides", "best", "better", "between", "big", "bird", "birth", "birthday", "bit", "bite", "black", "bleed","block", "blood", "blow", "blue", "board", "boat", "body", "boil", "bone", "book","border", "born", "borrow", "both", "bottle", "bottom", "bowl", "box","boy", "branch", "brave", "bread", "break", "breakfast", "breathe", "bridge", "bright", "bring", "brother", "brown","brush", "build", "burn", "business", "bus", "busy", "buy", "cake", "call", "can", "candle", "cap", "car", "card", "care", "careful", "careless", "carry", "case", "cat", "catch", "central", "century", "certain", "chair", "chance", "change", "chase", "cheap", "cheese", "chicken", "child", "children", "chocolate", "choice", "choose", "circle", "city", "class", "clever", "clean", "clear", "climb", "clock", "cloth", "clothes","cloud", "cloudy", "close", "coffee", "coat", "coin", "cold", "collect", "colour", "comb"," comfortable", "common", "compare", "come", "complete", "computer", "condition", "continue", "control", "cook", "cool", "copper", "corn", "corner", "correct", "cost", "contain", "count", "country", "course", "cover", "crash", "cross", "cry", "cup", "cupboard", "cut", "dance", "dangerous", "dark", "daughter", "day", "dead", "decide", "decrease", "deep", "deer", "depend", "desk", "destroy", "develop", "die", "different", "difficult", "dinner", "direction", "dirty", "discover", "dish", "do", "dog", "door", "double", "down", "draw", "dream", "dress", "drink", "drive", "drop", "dry", "duck", "dust", "duty", "each", "ear", "early", "earn", "earth", "east", "easy", "eat", "education", "effect", "egg", "eight", "either", "electric", "elephant", "else", "empty", "end", "enemy", "enjoy", "enough", "enter", "equal", "entrance", "escape", "even", "evening", "event", "ever", "every", "everyone", "exact", "everybody", "examination", "example", "except", "excited", "exercise", "expect", "expensive", "explain", "extremely", "eye","face", "fact", "fail", "fall", "false", "family", "famous", "far", "farm", "father", "fast", "fat", "fault", "fear", "feed", "feel", "female", "fever", "few", "fight", "fill", "film", "find", "fine", "finger", "finish", "fire", "first", "fish", "fit", "five", "fix", "flag", "flat", "float", "floor", "flour", "flower", "fly", "fold", "food", "fool", "foot", "football", "for", "force", "foreign", "forest", "forget", "forgive", "fork", "form", "fox", "four", "free", "freedom", "freeze", "fresh", "friend", "friendly", "from", "front", "fruit", "full", "fun", "funny", "furniture", "further", "future", "game", "garden", "gate", "general", "gentleman", "get", "gift", "give", "glad", "glass", "goat", "god", "gold", "good", "goodbye", "grandfather", "grandmother", "grass", "grave", "great", "green", "gray", "ground", "group", "grow", "gun", "hair", "half", "hall", "hammer", "hand", "happen", "happy", "hard", "hat", "hate", "have", "head", "healthy", "hear", "heavy", "heart", "heaven", "height", "hello", "help", "hen", "her", "here", "hers", "hide", "high", "hill", "him", "his", "hit", "hobby", "hold", "hole", "holiday", "home", "hope", "horse", "hospital", "hot", "hotel", "house", "how", "hundred","hungry", "hour", "hurry", "husband", "hurt","ice", "idea", "important",  "increase", "inside", "introduce", "invent", "iron", "invite", "island", "jelly", "job", "join", "juice", "jump", "just", "keep", "key", "kill", "kind", "king", "kitchen", "knee", "knife", "knock", "know", "ladder", "lady", "lamp", "land", "large","last", "late", "lately", "laugh", "lazy", "lead", "leaf", "learn", "leave", "leg", "left", "lend", "length", "less", "lesson", "let", "letter", "library", "lie", "life", "light", "like", "lion", "lip", "list", "listen", "little", "live", "lock", "lonely", "long", "look", "lose", "lot", "love", "low", "lower", "luck" ,"machine", "main", "make", "male", "man", "many", "map", "mark", "market", "marry", "matter", "may", "meal", "mean", "measure", "meat", "medicine", "meet", "member", "mention", "method", "middle", "milk", "million", "mind", "minute", "miss", "mistake", "mix", "model", "modern", "moment", "money", "monkey", "month", "moon", "more", "morning","most", "mother", "mountain", "mouth", "move", "much", "music", "must","name", "narrow", "nation", "nature", "near", "nearly", "neck", "need", "needle", "neighbour", "neither", "net", "never", "new", "news", "newspaper", "next", "nice", "night", "nine", "noble", "noise", "none", "nor", "north", "nose","nothing", "notice", "now", "number","obey", "object", "ocean", "offer", "office", "often", "oil", "old", "only", "open", "opposite", "orange", "order", "other", "outside", "over", "page", "pain", "paint", "pair", "pan", "paper", "parent", "park", "part", "partner", "party", "pass", "past", "path", "pay", "peace", "pen", "pencil", "people", "pepper", "per", "perfect", "period", "person", "petrol", "photograph", "piano", "pick", "picture", "piece", "pig", "pin", "pink", "place", "plane", "plant", "plastic", "plate", "play", "please", "pleased", "plenty", "pocket", "point", "poison", "police", "polite", "pool", "poor", "popular", "position", "possible", "potato", "power", "present", "press", "pretty", "prevent", "price", "prince", "prison", "private", "prize", "probably", "problem", "produce", "promise", "proper","protect", "provide", "public", "pull", "punish", "pupil", "push", "put", "queen", "question", "quick", "quiet", "quite", "radio", "rain", "rainy", "raise", "reach", "read", "ready","real", "really", "receive", "record", "red", "remember", "remind", "remove", "rent", "repair", "repeat", "reply", "report", "rest", "restaurant", "result", "return", "rice", "rich", "ride", "right", "ring", "rise", "road", "rob", "rock", "room", "round", "rubber", "rude", "rule", "ruler", "run", "rush", "sad", "safe", "sail", "salt", "same", "sand", "save", "say", "school", "science", "scissors", "search", "seat", "second", "see", "seem", "sell", "send","sentence", "serve", "seven", "several",  "shade", "shadow", "shake", "shape", "share", "sharp", "sheep", "sheet", "shelf", "shine", "ship", "shirt", "shoe", "shoot", "shop", "short", "should", "shoulder", "shout", "show", "sick", "side", "signal", "silence", "silly", "silver", "similar", "simple", "single", "since", "sing", "sink", "sister", "sit", "six", "size", "skill", "skin", "skirt", "sky", "sleep", "slip", "slow", "small", "smell", "smile", "smoke", "snow", "soap", "sock", "soft", "some", "someone", "something", "sometimes", "son", "soon", "sorry", "sound", "soup", "south", "space", "speak", "special", "speed", "spell", "spend", "spoon", "sport", "spread", "spring", "square", "stamp", "stand", "star", "start", "station", "stay", "steal", "steam", "step", "still", "stomach", "stone", "stop", "store","storm", "story", "strange", "street", "strong", "structure", "student", "study", "stupid", "subject", "substance", "successful", "such", "sudden", "sugar", "suitable", "summer", "sun", "sunny", "support", "sure", "surprise", "sweet", "swim", "sword", "table", "take", "talk", "tall","taste", "taxi", "tea", "teach", "team", "tear", "telephone", "television", "tell", "ten", "tennis", "terrible", "test", "there", "therefore", "these", "thick", "thin", "thing", "think", "third", "this", "though", "threat", "three", "tidy", "tie", "title", "today", "toe", "together", "tomorrow", "tonight","tool", "tooth", "top", "total", "touch", "town", "train", "tram", "travel", "tree", "trouble", "true", "trust", "twice", "try", "turn", "type", "ugly", "uncle", "under", "understand", "unit", "until", "use", "useful", "usual", "usually", 
"vegetable", "very", "village", "voice", "visit", "wait", "wake", "walk", "want", "warm", "wash", "waste", "watch", "water", "way", "weak", "wear", "weather", "wedding", "week", "weight", "welcome", "were", "well", "west", "wet", "what", "wheel", "when", "where", "which","while", "white", "who", "why", "wide", "wife", "wild", "will", "win", "wind", "window", "wine", "winter", "wire", "wise", "wish", "with", "without", "woman", "wonder", "word", "work", "world", "worry", "yard", "yell", "yesterday", "yet", "you", "young", "zero", "zoo"]

letter=[]

letterdrawer = turtle.clone()



drawing = turtle.clone()
# drawing.ht()

drawing.pu()
drawing.goto(-600,-200)
drawing.pd()
drawing.forward(300)
drawing.backward(150)
drawing.left(90)
drawing.forward(500)
drawing.right(90)
drawing.forward(200)
drawing.right(90)
drawing.forward(50)
turtle.getscreen().update()

i= random.randint(0,950)
word = words[i]
#to test you  can add the print word here

turtle.goto(0,-200)
for b in range(len (word)):
	turtle.pd()
	turtle.forward(50)
	turtle.pu()
	turtle.forward(30)


def playing ():
	global trys_left
	
	while trys_left>0:
		letter_given = str(input("guess a letter"))
		if letter_given in letter:
			print ("You already guessed that")
			letter_given = str(input("guess another letter"))

		letter.append(letter_given)

		if letter_given in word:
			print("TRUE")
			Trues = -1
			for u in range (len(word)):
				if letter_given == word[u]:
					letterdrawer.pu()
					letterdrawer.goto(0,-200)
					for g in range(u):
						letterdrawer.pu()
						letterdrawer.forward(50)
						letterdrawer.forward(30)
					letterdrawer.write(letter_given,move= False, font=("Papyrus", 20, "normal"))
			for i in range (len(word)):
				if word[i] in letter:
					Trues = Trues+1
					if Trues == u:
						title.pu()
						title.goto(-170,150)
						title.color("red")
						title.write("YOU WONNNNNN" ,move= False, font=("Papyrus", 40, "normal"))
						time.sleep(5)
						turtle.bye()

				else:
					
					break


		
				

		if str(letter_given)not in word:
			print("false")
			trys_left = trys_left-1
			title.clear()
			title.write("Trys Left = "+ str(trys_left) ,move= False, font=("Papyrus", 20, "normal"))
			if trys_left == 9:
				drawing.pu()
				drawing.right(90)
				drawing.forward(5)
				drawing.pd()
				drawing.circle(50)
				turtle.goto(0,-200)
				turtle.pd()
				turtle.forward(50)
			elif trys_left == 8:
				drawing.pu()
				drawing.goto(-255,150)
				drawing.left(90)
				drawing.pd()
				drawing.forward(200)
				
			elif trys_left == 7:
				drawing.left(45)
				drawing.forward(60)

			elif trys_left == 6:
				drawing.backward(60)
				drawing.right(90)
				drawing.forward(60)

			elif trys_left == 5:
			 	drawing.backward(60)
			 	drawing.left(45)
			 	drawing.backward(150)
			 	drawing.left(50)
			 	drawing.forward(80)

			elif trys_left == 4:
			 	drawing.backward(80)
			 	drawing.right(100)
			 	drawing.forward(80)

			elif trys_left == 3:
				drawing.pu()
				drawing.goto(-275,225)
				drawing.left(5)
				drawing.pd()
				drawing.forward(10)
				drawing.backward(5)
				drawing.left(90)
				drawing.forward(5)
				drawing.backward(10)
				drawing.pu()
				drawing.goto(-235,225)
				drawing.right(90)
				drawing.pd()
				drawing.forward(10)
				drawing.backward(5)
				drawing.left(90)
				drawing.forward(5)
				drawing.backward(10)

				



			elif trys_left == 2:
				drawing.pu()
				drawing.goto(-255,200)
				drawing.right(45)
				drawing.pd()
				drawing.forward(15)
				drawing.right(90)
				drawing.forward(5)
			


			elif trys_left == 1:
				drawing.pu()
				drawing.goto(-235,175)
				drawing.pd()
				drawing.forward(40)
		


			if trys_left == 0:
				drawing.backward(10)
				drawing.left(90)
				drawing.color("red")
				drawing.forward(5)
				for x in range(180):
					drawing.forward(0.15)
					drawing.left(1)
				drawing.forward(5)
				# time.sleep(1)
				title.pu()
				title.goto(-170,150)
				title.write("GAME OVER" ,move= False, font=("Papyrus", 40, "normal"))
				title.goto(-140,90)
				title.write("The word was : " + word,move= False, font=("Papyrus", 40, "normal"))
				time.sleep(4)
				turtle.bye()

		turtle.getscreen().update()



				#issue with tounge (the sleep function) i need an alternative
				


		



playing()

#ask about letters

turtle.mainloop()







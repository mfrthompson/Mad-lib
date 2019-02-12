# This is a little story while learning if statements.
def story():
	myName = input("Hello! What is your name?: ")
	question = input("Nice to meet you " + myName + "! Would you like to play a little game?")
	if(question != "yes" and question != "Yes" and question != "no" and question != "No"):
		print("I'm sorry, I should have said before only answer Yes or No please.")
		story("Lets try that one more time")
	elif(question == "no" or question == "No"):
		print("Thats OK " + myName + ", there's always next time.")
	elif(question == "yes" or question == "Yes"):
		print("Great " + myName + "! I think you'll enjoy the game!")
		print("Before we can get started " + myName + ", I'm going to ask a few questions to create a story about you!")
		year = int(input("What year were you born?:"))
		hometown = input("Great! A lot of cool things happened in " + str(year) + ". Now, what city were you born in?:")
		state = input("And what state is " + hometown + " in?:")
		print("It's very nice to meet you " + myName + " from " + hometown + ", " + state +"!")
		age = int(2019) - int(year)
		print("Well, if my math is correct you should be around " + str(age) + "years old.")


story()

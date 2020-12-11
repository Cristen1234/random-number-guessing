import random
low=int(input("Enter a minumum value for the range. "))
high=int(input("Enter the maximum value for the range. "))

#set up variable for computer
random_number=random.randint(low,high)


while True:
	try:
	#set up variable for player's guess
		guess=int(input(f"Enter a number between {low} and {high}: "))
	except:
		print("Type a whole number instead: ")
		continue #return to beginning of the loop
	#compare the two variables


	if guess==random_number:
		print("You guessed correctly!")
		break
	elif guess>random_number:
		print("Your guess is too high. ")
	else:
		print("Your guess is too low. ")




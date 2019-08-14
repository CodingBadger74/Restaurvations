#imports the ability to get a random number (we will learn more about this later!)
from random import *

# For Testing: print(aRandomNumber)
def playAgain():
	answer = input("Would you like to play again? ")
	if answer.lower().startswith('y'):
		print()
		play(guesses, high)
	else:
		exit()

def play(guesses, high):
	aRandomNumber = random.randint(1, high)
	for i in range(guesses):
		guess = ''
		while not guess.isnumeric(): # checks if a string is only digits 0 to 9
			guess = input("Guess a number between 1 and " + str(high) + " (inclusive): ")
			if not guess.isnumeric():
				print("That's not a positive whole number, try again!")
		else:
			guess = int(guess) # converts a string to an integer
			if guess > aRandomNumber:
				print("Too high!", end = '')
				if i < (guesses - 1):
					print(' Try again!')
				else:
					print(' Out of guesses.')
			elif guess < aRandomNumber:
				print("Too low!", end = '')
				if i < (guesses - 1):
					print(' Try again!')
				else:
					print(' Out of guesses.')
			elif guess == aRandomNumber:
				print("You won in", i + 1, "guesses!")
				playAgain()
		if i == (guesses - 1):
			playAgain()

answer = input("Would you like to play easy, medium, or hard? ")
if answer.lower().startswith('e'):
	guesses = 6; high = 30
elif answer.lower().startswith('m'):
	guesses = 5; high = 40
elif answer.lower().startswith('h'):
	guesses = 3; high = 40
play(guesses, high)

import random

# A list of words that
potential_words = ["sasparilla", "geronimo", "abibliophobia", "bumfuzzle", "cattywampus", 'gardyloo', 'taradiddle', 'snickersnee', 'widdershins', 'collywobbles', 'gubbins', 'bumbershoot', 'lollygag', 'flibbertigibbet', 'malarkey', 'pandiculation', 'sialoquent', 'wabbit', 'snollygoster', 'erinaceous', 'bibble', 'impignorate', 'nudiustertian', 'quire', 'ratoon', 'yarborough', 'xertz', 'zoanthropy', 'pauciloquent', 'bloviate', 'borborygm', 'brouhaha', 'absquatulate', 'comeuppance', 'donnybrook', 'nincompoop']

word = random.choice(potential_words)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = []
for letter in word:
	current_word.append('_')
	#"_", "_"] # TIP: the number of letters should match the word

# Some useful variables
maxfails = 7
fails = 0

lettersLeft = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
allLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

level = input("Welcome to Hangman! Would you like to play easy, medium, or hard? \n")

if level[0].lower() == 'e':
	maxfails = 15
elif level[0].lower() == 'm':
	maxfails = 10
else:
	maxfails = 7

print()
for letter in current_word:
	print(letter, end = ' ')
print()
print()

while fails < maxfails:
	print("You have " + str(maxfails - fails) + " tries left!")

	correct = 0
	guess = input("Guess a letter: ")
	numCorrect = 0

	# check if the guess is valid: Is it one letter? Have they already guessed it?
	if len(guess) != 1 or guess.lower() not in allLetters:
		print("Not a valid answer. Please try again with one letter.")
	elif guess.lower() not in lettersLeft:
		print("You've already guessed that. Please guess a new letter.")
	# check if the guess is correct: Is it in the word? If so, reveal the letters!
	else:
		lettersLeft.remove(guess)
		print()
		for letter in range(0, len(word)):
			if guess == word[letter]:
				current_word[letter] = word[letter]
				correct += 1
			print(current_word[letter], end = ' ')
			if current_word[letter] == word[letter]:
				numCorrect += 1
		print()
		print()
		if correct < 1:
			fails += 1
		if numCorrect == len(word):
			print("You win!!!")
			break
		if fails == maxfails:
			print('You lose :( \nThe answer was', word.upper() + '.')

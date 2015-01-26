#!/usr/bin/python3

import random

HANGMAN = (
"""
____________
|   
|   
| 
|  
|
|
|___________

""",
"""
____________
|   |
|   
|  
| 
|
|
|___________

""",

"""
____________
|   |
|   0
|  
|  
|
|
|___________

""",
"""
____________
|   |
|   0
|  /
|  
|
|
|___________

""",
"""
____________
|   |
|   0
|  / \\
|  
|
|
|___________

""",
"""
____________
|   |
|   0
|  /|\\
|  
|
|
|___________

""",

"""
____________
|   |
|   0
|  /|\\
|  / 
|
|
|___________

""",
"""
____________
|   |
|   0
|  /|\\
|  / \\
|
|
|___________

"""
)


WORDS = ("banana","monkey","titanic","catastrophy","symphonic",
	"computer","television")


def displayHangman(numbersGuessed, guessedSoFar):
	print(HANGMAN[numbersGuessed])

	print("You have ", 8 - numbersGuessed, "  guesses left")
	print("Here's the word so far: ")
	print("\n\n\n")
	for score in guessedSoFar:
		print(score," ", end = "")
	print("\n")



def getPlayerGuess(numbersGuessed, guessedSoFar, correctWord):

	userInput = input("""
		Input 1 then press Enter to guess the LETTER
		Input 2 then press Enter to guess the WORD
		"""
		)

	while(userInput != '1' and userInput != '2'):
		userInput = input("""
		Input 1 then press Enter to guess the LETTER
		Input 2 then press Enter to guess the WORD
		"""
		)


	if(userInput == '1'):
		letterGuess = input("What LETTER would you like to guess?")
		while(len(letterGuess) > 1 ):
			print("Please input a letter, not a string")
			letterGuess = input("What LETTER would you like to guess?")
		counter = 0
		guessedACorrectWord = False
		for letter in correctWord:
			if letter == letterGuess:
				guessedSoFar[counter] = letter
				guessedACorrectWord = True
			counter = counter + 1
		if(guessedACorrectWord == False):
			numbersGuessed = numbersGuessed + 1
		return numbersGuessed



	elif(userInput == '2'):
		print("nothing for now")




def main():



	input("""
		Welcome to the HANGMAN game!
		The goal is to try to guess 
		the word, before this poor guy
		gets hanged. Everytime you guess 
		something wrong another limb
		of the stickman will appear. 
		If all of the stickman appears, you
		lose! You have 7 guesses in total! 
		After the 6th wrong guesses you 
		will recieve a HINT

		PRESS ENTER TO BEGIN
		""")


	print("""
-----------------------------------------------------------

		""")

	correctWord = random.choice(WORDS)
	guessedSoFar = []

	for i in range(len(correctWord)):
		guessedSoFar.append('_')
	numbersGuessed = 0


	while(numbersGuessed < 8):
		displayHangman(numbersGuessed, guessedSoFar)
		numbersGuessed = getPlayerGuess(numbersGuessed,guessedSoFar, correctWord)




	




main()
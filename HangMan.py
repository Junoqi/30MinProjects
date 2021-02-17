#Imports
import random
import replit

#Global Variables
words = ["Cat", "Bat", "Ace", "Act", "App", "Cap"]

#Speech
def start():
  print("Welcome to HANGMAN!")
  print("Selecting word...")
  print("Word selected.")
  print("")
  play()

#Game loop
def play():
  word = random.choice(words)
  print("Word: " + "*" * len(word))

  guesses = 10
  guessedLetters = ""
  while guesses > 0:
    print("Guess!")
    wordGuess = ""
    guess = input()
    print("---")

    if(guess == word.lower()):
      replit.clear()
      print("")
      print("YOU WON!")
      print(f"The word was: {word}")
      playAgain()

    elif(len(guess) > len(word)):
      print("Guess is larger than the word...")
      print("")
      continue

    for char in word.lower():
      if(char == guess):
        wordGuess += char
      else:
        wordGuess += "*"

    print("Word: " + wordGuess)

    guesses += -1

    if(guess in guessedLetters):
      guesses += 1
      pass
    else:
      guessedLetters += guess

    print(f"Guesses Left: {guesses}")
    print(f"Guessed Letters: {guessedLetters}")
    print("")

  if(guesses == 0):
    replit.clear()
    print("")
    print("YOU LOST!")
    playAgain()
    
#Play again loop
def playAgain():
  print("Play again? (Y/N)")
  again = input()
  if(again.lower() == "y"):
    replit.clear()
    start()
  elif(again.lower() == "n"):
    exit()
  else:
    exit()

start()
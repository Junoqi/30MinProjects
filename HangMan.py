#Imports
import random
import replit
import time

#Global Variables
words = ["Cat", "Bat", "Ace", "Act", "App", "Cap"]

#Speech
def start():
  print("Welcome to HANGMAN!")
  print("Selecting word...")
  print("Word selected.")
  print("")
  time.sleep(1.5)
  play()


def split(word): 
    return list(word) 

#Game loop
def play():
  guessed = []

  word = random.choice(words)
  wordList = split(word)
  replit.clear()
  print("Word is " + str(len(word)) + " letters long")
    
  guesses = 10
  guessedLetters = ""
  while guesses > 0:
    print("Guess!")
    wordGuess = ""
    guess = input()
    print("---")

    for char in word.lower():
      if(char == guess):
        guessed.append(char.lower())
      else:
        pass

    for char in wordList:
      if(char.lower() in guessed):
        wordGuess += char
      else:
        wordGuess += "*"

    if(guess == word.lower()):
      replit.clear()
      print("")
      print("YOU WON!")
      print(f"The word was: {word}")
      playAgain()

    if("*" not in wordGuess):
      replit.clear()
      print("")
      print("YOU WON!")
      print(f"The word was: {word}")
      playAgain()

    elif(len(guess) > len(word)):
      print("Guess is larger than the word...")
      print("")
      continue

    elif(len(guess) > 1):
      print("Guess can't be larger than 1")
      print("")
      continue


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
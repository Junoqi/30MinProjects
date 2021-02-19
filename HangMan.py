#Imports
import random
import replit
import time
import sys
import os

#Global Variables
words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks' ] 
animation = words


#Clear function
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

#Speech
def start():
  print("Welcome to HANGMAN!")
  for i in range(30):
    time.sleep(0.1)
    sys.stdout.write("\rSelecting word: " + animation[i % len(animation)])
    sys.stdout.flush()
    #do something
  print("\nWord selected.")
  time.sleep(1.5)
  play()

def split(word): 
    return list(word) 

#Game loop
def play():
  guessed = []
  word = random.choice(words)
  wordList = split(word)
  try:
      replit.clear()
  except:
      cls()

  print("Word is " + str(len(word)) + " letters long")

  guesses = len(word) + 5
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

    if("*" not in wordGuess):
      try:
          replit.clear()
      except:
          cls()
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
    print("Last chance!")
    print("Guess the word: ") 
    finalGuess = input()
    if(finalGuess == word):
      win()
    else:
      lose()

#Win function
def win():
  try:
      replit.clear()
  except:
      cls()
  print("")
  print("YOU WON!")
  playAgain()

#Lose function
def lose():
  try:
      replit.clear()
  except:
      cls()
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
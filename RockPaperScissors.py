import random
import replit
import os


#Global Variables
options = ["Rock", "Paper", "Scissors"]

#Clear function
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#In a function so i can loop
def start():
  print("WELCOME TO ROCK PAPER SCISSORS! ")
  play("play")

#Player Win
def playerWin():
  print("You won!! Play again? (Y/N): ")
  playAgain = input()

  if(playAgain.lower() == "y"):
    try:
      replit.clear()
    except:
      cls()
    start()

  elif(playAgain.lower() == "n"):
    return
#CPU Win
def cpuWin():
  print("Uh-oh! You lost!! Play again? (Y/N): ")
  playAgain = input()

  if(playAgain.lower() == "y"):
    try:
      replit.clear()
    except:
      cls()
    start()
  elif(playAgain.lower() == "n"):
    return

#Game Loop
def play(type):
  if(type == "again"):
    print("Same Input! Again!")
  else:
    pass

  cpuChoice = random.choice(options)
  #PlayerInput
  print("Rock, Paper or Scissors?: ")
  playerChoice = input()

  #Speech
  print("-------")
  print("Rock...")
  print("Paper...")
  print("Scissors...")
  print("SHOOT!")
  print("-------")

  print(f"{playerChoice.upper()} (You) VS {cpuChoice.upper()} (CPU)")

  print("-------")

  #Logic
  if(cpuChoice.lower() == playerChoice.lower()):
    try:
      replit.clear()
    except:
      cls()
    play("again")
  elif(cpuChoice.lower() == "rock" and playerChoice.lower() == "paper"):
    playerWin()
  elif(cpuChoice.lower() == "paper" and playerChoice.lower() == "scissors"):
    playerWin()
  elif(cpuChoice.lower() == "scissors" and playerChoice.lower() == "rock"):
    playerWin()
  elif(cpuChoice.lower() == "paper" and playerChoice.lower() == "rock"):
    cpuWin()
  elif(cpuChoice.lower() == "rock" and playerChoice.lower() == "scissors"):
    playerWin()
  elif(cpuChoice.lower() == "scissors" and playerChoice.lower() == "paper"):
    playerWin()
  else:
    print("INVALID INPUT")
    play("play")

start()

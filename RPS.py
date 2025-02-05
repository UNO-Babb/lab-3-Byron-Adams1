#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  play = "Yes"
  while (play == "Yes"): # check the variable
    #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
    player = input  ("Enter Rock (R), Paper (P), or Scissors(S)")
    
    computer = random.choice= ["R", "P", "S"]
    
    if player == "R":
      print ("Player chose ROCK") 
    if player == "P":
      print ("Player chose PAPER")
    if player == "S":
      print ("Player chose SCISSORS")
    if player == computer:
      print ("TIE")
      ties = ties + 1
    elif player == "R" and computer == "S" :
      print ("You win!")
      wins = wins + 1
    elif player == "R" and computer == "P":
      print ("You lose!")
      losses = losses + 1
    elif player == "P" and computer == "S":
      print ("You lose!")
      losses = losses + 1
    elif player == "S" and computer == "R":
      print ("You Lose!")
      losses= losses + 1


  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

    answers = [ "Rock", "Paper", "Scissors"]
  
       #Rock, Paper, Scissors Game
  play = input("Play again? (Y/N): ") #change the variable
  
  print("End of the game.")
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)
  response = random.choice(answers)
  print (response)

if __name__ == '__main__':
  main()

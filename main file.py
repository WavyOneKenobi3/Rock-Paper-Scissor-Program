import random

#list of choices 
  selections = ["Rock", "Paper", "Scissors"]



#player input for selection
def selection_player(): 
  user_picks = input("Please select between Rock, Paper and Scissors: ").capitalize()
  while user_picks not in selections:
    print("Not one of the selection, select again")
    user_picks = input("Please select between Rock, Paper and Scissors: ").capitalize()
  return user_picks


def rules_game():
  #computer random selection
  computer_picks = random.choice(selections)
  # Get player's selection
  player1_picks = selection_player()
  
  if player1_picks == computer_picks:
    print(f"Draw \n Player: {player1_picks} vs  Computer: {computer_picks}")
  elif (player1_picks == "Rock" and computer_picks == "Scissors") or (player1_picks == "Scissors" and computer_picks == "Paper") or (player1_picks == "Paper" and computer_picks == "Rock"):
    print(f"Player Wins \n {player1_picks} vs {computer_picks}")
  else:
    print(f" Computer Wins \n Computer: {computer_picks} vs\nPlayer: {player1_picks}")


    
def play_game(): 
  #loop asking to continue playing
  while True:
    rules_game()
    
    user_responds = input("\n Do you want to Play Yes or No? ").strip().lower()
    
    if user_responds == "yes":
      continue
    elif user_responds == "no":
      print("\n Thank you for playing")
      break
    else:
      print("not a selection")

play_game()

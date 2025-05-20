import random

#list of choices 
  selections = ["Rock", "Paper", "Scissors"]

Winning_picks = {
  "Rock":"Scissors",
  "Paper":"Rock",
  "Scissors":"Paper"
}



#player input for selection
def get_player_choice():
    While True:
      user_picks = input("Please select between Rock, Paper and Scissors: ").strip().capitalize()
      if user_picks in selec
      return user_picks


def determine_winner(player_choice, computer_choice):
  if player_choice == computer_choice:
    return "Draw"
  elif  Winning_picks[player_choice] == computer_choice:                        #statement is comparing answers and if its true or false
    return "Player Wins"
  else:
    return "Computer Wins"

def play_round():
  #computer random selection
  computer_choice = random.choice(selections)
  # Get player's selection
  player1_picks = get_player_choice()
  #
  result = determine_winner(player1_picks, computer_choice)

  # Display the result    
  print(f"\n{result}!\nPlayer: {player1_picks} vs Computer: {computer_choice}")
    
def play_game(): 
  #loop asking to continue playing
  while True:
    play_round()
 
    play_again = input("\n Do you want to Play Yes or No? ").strip().lower()
    
    if user_responds == "yes":
      continue
    elif user_responds == "no":
      print("\n Thank you for playing")
      break
    else:
      print("not a selection")

play_game()

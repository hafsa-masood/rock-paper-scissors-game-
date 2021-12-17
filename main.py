import random 

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

rock_paper_scissors_list = ['rock','paper','scissors']

def is_correct_input(player_choice):
  return player_choice == 'rock' or player_choice == 'paper' or player_choice == 'scissors'
  
def is_wrong_input(player_choice):
  return player_choice != 'rock' and player_choice != 'paper' and player_choice != 'scissors'

def take_player1_input():
  player1_input = ''
  while is_wrong_input(player1_input):
    print("Please choose a valid input")
    player1_input = input('Choose rock, paper, or scissors: ').lower() 
  if is_correct_input(player1_input):
    return player1_input
  
def computer_choice():
  computer_choice = random.choice(rock_paper_scissors_list)
  return computer_choice

def who_won(player1_input, computer_choice):
  print(f"Computer chooses {computer_choice}")
  if player1_input == computer_choice:
    print("It's a tie!")
  elif player1_input == ROCK and computer_choice == SCISSORS:
    print(f"{ROCK} beats {SCISSORS}. Player 1 wins!")
  elif player1_input == ROCK and computer_choice == PAPER:
    print(f"{PAPER} beats {ROCK}. Computer wins!")
  elif player1_input == PAPER and computer_choice == ROCK:
    print(f"{PAPER} beats {ROCK}. Player 1 wins!")
  elif player1_input == PAPER and computer_choice == SCISSORS:
    print(f"{SCISSORS} beats {PAPER}. Computer wins!")
  elif player1_input == SCISSORS and computer_choice == PAPER:
    print(f"{SCISSORS} beats {PAPER}. Player 1 wins!")
  elif player1_input == SCISSORS and computer_choice == ROCK:
    print(f"{ROCK} beats {SCISSORS}. Computer wins!")

def continue_play_choice():
  choice = 'WRONG'
  choice_options = ['Y','N']
  while choice not in choice_options:
    choice = input('Do you want to keep playing? (Y or N): ').upper()
    if choice not in choice_options:
      print("Sorry, I didn't understand. Please choose Y or N")
  
  if choice == 'Y':
    return True 
  else:
    return False
    
def lets_play():
  game_on = True
  print("Welcome to Rock, Paper, Scissors! You will be playing against a computer.") 
  while game_on:
    p1_input = take_player1_input()
    cp_input = computer_choice()
    who_won(p1_input, cp_input)
    game_on = continue_play_choice()
  if game_on == False:
    print('Goodbye!')


lets_play()

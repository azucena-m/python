import random
#generate a random choice from a list of rock, paper, scissors
#ask player to choose option r/p/s
#if random choice equals player choice, print Tie
#if random choice is rock
#   player choice is paper, print you win
#   player choice is scissors, print you lose
#if random choice is p, 
#   playerchoice is rock = you lose
#   playerchoice is s = you win
#if randomchoice is s,
#   playerchoice is r = you win
#   playerchoice is p = you lose
#afeter each choice ask player if they want to continue, loop

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = { PAPER: '📃', SCISSORS: '✂️',  ROCK: '🪨'}
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        player_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if player_choice in choices:
            return player_choice   
        else:
            print('invalid choice')

def display_choices(player_choice, computer_choice):
    print(f'You chose {emojis[player_choice]}')
    print(f'computer chose {emojis[computer_choice]}')        

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print('you tied')
    elif (
        (player_choice == ROCK and computer_choice == SCISSORS) or
        (player_choice == SCISSORS and computer_choice == PAPER) or
        (player_choice == PAPER and computer_choice == ROCK)):
        print('you win')
    else:
        print('you lose')

def play_game():
    while True:
        player_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(player_choice, computer_choice)

        determine_winner(player_choice, computer_choice)

        continue_game = input('Do you want to play again? (y/n) ').lower()
        if continue_game == 'n':
            break
    
play_game()
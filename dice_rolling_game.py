#ask player if they want to roll the dice
#choices are yes or no (y/n)
import random


#if the player picks any other option print 'invalid choice!
#if the player picks y, roll the dice using random numbers from 1-6, and print two random numbers
#if the player picks n, print 'Thanks for playing! 
game = 0
while game <= 4:
    if game == 4:
        break
    game += 1
    player_choice = input('Roll the dice? (y/n): ').lower()
    if player_choice == 'y':
        # print(f'{(random.randint(1,6), random.randint(1,6))}')
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1}, {die2})')
        
    elif player_choice == 'n':
        print("Thank's for playing!")
        break
    else:
        print('invalid choice!')
#generate random number
#need to ask user to guess a number between 1 and 100
#need a loop to repeat the program until the numbe is guessed
#if the number is guessed is higher than our number, print Too high!
#if the number is lower than our number, print too low!
#if the number is guessed correctly, print congrats message

import random
right_number = random.randint(1,100)

while True:
    try: 
        guess_number = int(input('Guess the number between 1 and 100: ')) #for try blocks, the if has to be placed inside the try, otherwise the guess_number variable will not be available outside of it

        if guess_number < right_number:
            print('Too low!')
        elif guess_number > right_number:
            print('Too high!')
        else:
            print('Congratulations! You guessed the number.')
            break
    except ValueError:
        print('Not a valid number')

    
        
    
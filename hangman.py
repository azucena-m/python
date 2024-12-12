from words import words 
import random
import string

words = ['python', 'java', 'javascript', 'ruby', 'react', 'express']

chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word] #create a list of underscore per letter in chosen_word
attempts = 8

print('Welcome to Hangmain!')

while attempts > 0 and '_' in word_display:
    print('\n' + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] == guess #reveal letter
    else:
        print('That letter does not appear in the word')
        attempts -= 1
        
if '_' not in word_display:
    print('You guessed the word!')
    print(' '.join(word_display))
    print('You survived!')
else:
    print('You ran out of attempts. The word was: ' + chosen_word)
    print('You lost!')



# def get_valid_word(words):
#     word = random.choice(words)
#     while '-' in word or ' ' in word:
#         word = random.choice(words)
    
#     return word

# def hangmain():
#     word = get_valid_word(words)
#     word_letters = set(word)
#     alphabet = set(string.ascii_uppercase)
#     used_letters = set()

#     user_letter = input('Guess a letter: ').upper()

#     if user_letter in alphabet - used_letters:
#         used_letters.add(user_letter)
#         if user_letter in word_letters:
#             word_letters.remove(user_letter)
#     elif user_letter in used_letters:
#         print('You have already used that character. Please try again. ')
#     else:
#         print('Invalid character. Please try again. ')

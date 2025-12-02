import logic.logic as lg
import random
import os

# word_bank = [
#     "python", "jungle", "pizza", "robot", "galaxy", "tiger", "island", "coffee",
#     "rocket", "castle", "banana", "forest", "keyboard", "dragon", "whale", "piano",
#     "desert", "monitor", "ocean", "cookie", "eagle", "volcano", "battery", "wizard",
#     "mountain", "internet", "storm", "guitar", "lion", "panda", "treasure", "engine",
#     "river", "satellite", "ship", "sandwich", "shark", "planet", "camera", "bridge"
# ]
word_bank = [
    "python"
]

# note = ''' 
#     Note:
#     Wrong guesses draw parts of the hangman.
#     Finish the word before the figure completes.
# '''    

def clear_screan():
    if os.name == 'nt':
        os.system('cls') # Windows Users
    else:
        os.system('clear') # Linux Users
        
def press_enter():
    input('\nPress Enter to Continue...')
    
def word_update(game_word, guess, current_state):
    new_state = list(current_state)
    
    for i, letter in enumerate(game_word):
        if letter == guess:
            new_state[i] = guess
    
    return ''.join(new_state)

 

def menu():
    run = True
    while run:
        clear_screan()
        print('1. Start Game...')
        print('2. Save Results.')
        print('3. Exit.')
        print('*' * 50)
        
        try:
            choice = int(input('Enter number of the option(1, 2, 3) '))
            if choice <= 3 and choice >=1:
                if choice == 1:
                    game(choice)
                
            else:
                print('Enter number between 1 to 3...')
                
        except ValueError:
            print('Enter NUMBER...')

def game(choice):
    clear_screan()
    game_logic = lg.logic()
    game_word = random.choice(word_bank).lower()
    count = 0 
    
    # Print _ _ _ _
    current_state = '_' * len(game_word) 
    word = [current_state]
    print(' '.join(current_state))
    
    print(lg.hangman_ascii[0]) # Print hangman[0]
         
    while True:
        guess = input('\nEnter Your Guess(a-z) : ').lower().strip()
        
        if len(guess) == 1 and guess.isalpha():
            result, hangman, attempt = game_logic.win(guess, game_word, count)
            
            if result == False:
                count = attempt
                print('Nope...')
                
            else:
                print('Good guess :) ')
            
            if count != 0:
                print(hangman)
            
            current_state = word_update(game_word, guess, current_state)
            word = [current_state]
            if word[0] == game_word:
                clear_screan()
                print('Word : ', word[0])
                print('You Won...')
                press_enter()
                break
                         
        else:
            print('Enter the letter not word or something else...')
            count += 1
            
        if count == 6:
            print('You do not have any chance.')
            print('TRY AGAIN...')
            press_enter()
            break

        press_enter()
        clear_screan()
        print(' '.join(word[0]))
    
if __name__ == '__main__':
    game(3)    

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

note = '''
-> Note:
Your job is simple:
* Guess the word.
* Don't let the dude die.
* Stop typing random nonsense. Thanks.'''

start_game = '''
Welcome, mighty letter wizard!
A word is hiding. A stickman is panicking.
Try not to destroy his day, okay?
'''

def clear_screan():
    if os.name == 'nt':
        os.system('cls') # Windows Users
    else:
        os.system('clear') # Linux Users
        
def press_enter():
    input('\nPress Enter to Continue...\n(Yes, THAT Enter. Don\'t overthink it.)')
    
def word_update(game_word, guess, current_state):
    new_state = list(current_state)
    
    for i, letter in enumerate(game_word):
        if letter == guess:
            new_state[i] = guess
    
    return ''.join(new_state)

def menu():
    while True:
        clear_screan()
        print('/' * 25)
        print('1. Start Game...')
        print('2. Save Results.')
        print('3. Exit.')
        print('/' * 25)
        
        try:
            choice = int(input('Enter number of the option(1, 2, 3) '))
            if choice <= 3 and choice >=1:
                if choice == 1:
                    game(choice)
                elif choice == 2:
                    pass
                else:
                    break
                
            else:
                print('Enter number between 1 to 3...')
                
        except ValueError:
            print('Enter NUMBER...')

def game(choice):
    clear_screan()
    print(start_game)
    press_enter()
    clear_screan()
    game_logic = lg.logic()
    game_word = random.choice(word_bank).lower()
    count = 0 

    print(lg.hangman_ascii[0]) # Print hangman[0]
    print(note)
    press_enter()
    clear_screan()
    
    # Print _ _ _ _
    current_state = '_' * len(game_word) 
    word = [current_state]
    print(' '.join(current_state))
    
    while True:
        guess = input('\nEnter Your Guess(a-z) : ').lower().strip()
        
        if len(guess) == 1 and guess.isalpha():
            result, hangman, attempt = game_logic.win(guess, game_word, count)
            
            if result == False:
                count = attempt
                print('-> Wrong guess!\nStickman took emotional damage.')
                
            else:
                print('-> Nice! You actually guessed something right!\nStickman is relieved... for now.')
            
            if count != 0:
                print(hangman)
            
            current_state = word_update(game_word, guess, current_state)
            word = [current_state]
            if word[0] == game_word:
                clear_screan()
                print('Word : ', word[0])
                print('-> YOU WON!\nStickman lives another day!\nHe says “thanks” (or he would, if he had a mouth)')
                press_enter()
                break
                         
        else:
            print('-> WOW. Incredible.\nYou typed something that is not a letter at all.\nStickman is judging you silently.')
            count += 1
            print(lg.hangman_ascii[count])
            
        if count == 6:
            print('-> Welp… he\'s dead now.\nHope you\'re proud of yourself')
            print('TRY AGAIN...')
            press_enter()
            break

        press_enter()
        clear_screan()
        print(' '.join(word[0]))
    
if __name__ == '__main__':
    menu()    

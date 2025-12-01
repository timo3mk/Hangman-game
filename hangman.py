from logic import logic
import random
import os

def clear_screan():
    if os.name == 'nt':
        os.system('cls') # Windows Users
    else:
        os.system('clear') # Linux Users
        
def press_enter():
    input('\nPress Enter to Continue...')

def menu():
    print('1. Start Game...')
    print('2. Save Results.')
    print('3. Exit.')
    
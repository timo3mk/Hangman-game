import csv

hangman_ascii = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

class logic():
        
    def win(self, guess = '', game_word = '', attempt = 6):
        if guess in game_word:
            return guess
        else:
            return hangman_ascii[attempt]
        
    def save_results(self):
        with open('save.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            
p = logic()

print(p.win('c' ,'ali', 4))
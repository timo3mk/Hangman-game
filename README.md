# 🕹️ Hangman Game (Python)

A fun and interactive command-line Hangman game written in Python.  
This project includes a modular structure, ASCII-art hangman graphics, score saving, input validation, and a clean UI flow.

## 📌 Features
- 🎯 Random word selection from a built-in word bank  
- 💀 ASCII hangman graphics updated with each wrong guess  
- 🧠 Smart input validation (only single alphabetic letters)  
- 💾 Save game results to `save.csv`  
- 🧩 Modular code structure (`logic` module + main script)  
- 🔄 Clean menu (Start Game / Save Results / Exit)  
- 🧼 Works on Windows & Linux (auto screen clear)

## 📁 Project Structure
```
Hangman Game/
│
├── logic/
│   ├── __init__.py         # Makes 'logic' a package
│   └── logic.py            # Game logic + ASCII art + CSV saving
│
├── hangman.py              # Main game script (was main.py)
├── .gitignore              # Git ignore file
└── README.md               # Project documentation
```

---

## 🎥 Demo

<p align="center">
  <kbd>
    <img src="assets/Hangman_Demo.gif" width="400">
  </kbd>
</p>

<p align="center">
  <em>Quick demo of the Hangman gameplay — guessing letters, ASCII updates, and win/lose logic.</em>
</p>

---

## 🚀 How to Run

### 1. Clone the repository
```
git clone https://github.com/AliBahrami-ce/Hangman-game.git
cd Hangman-game
```
### 2. Run the game
```
python main.py
```
## 🎮 How the Game Works

### 🟢 Start Game
You will see:
- Intro message  
- First hangman ASCII frame  
- A hidden word displayed as `_ _ _ _`

### 🟡 Gameplay Rules
- Enter **one letter** at a time  
- Correct guess → updates the hidden word  
- Wrong guess → updates Hangman  
- You have **6 attempts**

### 🔴 Lose Condition
If attempts reach 6 → the stickman dies (**L**)

### 🟢 Win Condition
If you guess all letters → you win (**W**)

## 📊 Saving Results
Choosing option **2 – Save Results** writes a CSV file:
`
save.csv
`
### Format:

| # | Word   | W/L |
| - | ------ | --- |
| 1 | python | W   |
| 2 | robot  | L   |

## 🧱 Code Overview

### `main.py`
Handles:
- Menu  
- UI  
- Word selection  
- Input validation  
- Game loop  

### `logic/logic.py`
Contains:
- ASCII hangman frames  
- `logic` class  
- Correct/wrong guess handling  
- Saving results to CSV  

## 📦 Requirements
- Python **3.8+**  
- No external dependencies  

## 🛠️ Future Improvements (Ideas)
- Difficulty levels  
- GUI version (Tkinter / PyGame)  
- Sound effects  
- Load word list from external file  
- Show stats  
- "Play again" option  
- Unit tests  

## 🤝 Contributing
Pull requests are welcome!  
Open an issue if you want to suggest improvements or report bugs.

## 📜 License
This project is licensed under the **MIT License**.  
See the `LICENSE` file for details.

## 👤 Author
**Ali Bahrami**  
GitHub: https://github.com/AliBahrami-ce



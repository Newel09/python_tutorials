# Number Guessing Game (Python Match–Case)

A simple command-line number guessing game written in Python.  
The computer secretly picks a random number, and you have to guess it.  
Your guess is checked using Python’s `match`–`case` statement, and you can choose to play as many rounds as you like.

---

## Features

- Uses Python’s built-in `random` module  
- Generates a secret number with `random.randint()`  
- Uses `match`–`case` to compare the user’s guess with the secret number  
- Friendly messages if your guess is:
  - Correct  
  - Too high  
  - Too low  
- Option to play again at the end of each round

---

## Requirements

- Python 3.10 or later (for the `match`–`case` statement)
- A terminal or command prompt

---

## How to Run

1. Save the Python file as, for example:

   ```bash
   number_guessing_game.py

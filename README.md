# Tic Tac Toe

A simple command-line Tic Tac Toe game in Python. Play against the computer or another person on the same keyboard.

## Requirements

- Python 3

## How to run

From the project folder:

```bash
python tictactoe.py
```

## How to play

1. Choose a mode:
   - `1` — play against the computer (you are **X**, the computer is **O**)
   - `2` — two players on the same board
2. On your turn, enter a **row** and **column** as two numbers from `1` to `3`, separated by a space.  
   Example: `1 2` places a mark in the first row, second column.
3. The game ends when someone gets three in a row (row, column, or diagonal) or the board is full (draw).

Invalid input (wrong format, out of range, or an occupied cell) is rejected and you are asked again.

The in-game prompts are in Hebrew.

## Files

- `tictactoe.py` — game logic: board display, win/draw checks, human moves, and random computer moves

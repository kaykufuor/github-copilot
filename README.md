# Rock Paper Scissors (Tkinter)

A simple Python GUI Rock-Paper-Scissors game built with Tkinter.

## Features

- Play against a computer that picks randomly.
- Buttons for **Rock**, **Paper**, and **Scissors**.
- Round result display (win, lose, tie).
- Detailed scoreboard tracking:
  - Player wins
  - Computer wins
  - Ties
- **Reset** button to clear scores and reset labels.
- **Quit** button to close the app.

## Requirements

- Python 3.x
- Tkinter (included with most standard Python installations)

## Run the game

From the project folder, run:

```powershell
python rock_paper_scissors.py
```

If you use a virtual environment, activate it first or run with your environment's Python executable.

## How to play

1. Click **Rock**, **Paper**, or **Scissors**.
2. The app shows the computer's choice.
3. The app displays the round result.
4. The scoreboard updates after every round.

## Rules

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- Same choice = Tie

## Project structure

- `rock_paper_scissors.py` — main Tkinter application

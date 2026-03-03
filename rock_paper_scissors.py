"""Simple Tkinter Rock-Paper-Scissors game with score tracking."""

import random
import tkinter as tk


CHOICES = ["rock", "paper", "scissors"]


class RockPaperScissorsApp:
    """GUI application for playing Rock-Paper-Scissors against the computer."""

    def __init__(self, root: tk.Tk) -> None:
        """Build and initialize the game window and widgets."""
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("360x280")

        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0

        title_label = tk.Label(
            root, text="Rock Paper Scissors", font=("Segoe UI", 16, "bold")
        )
        title_label.pack(pady=10)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=8)

        tk.Button(
            button_frame, text="Rock", width=10, command=lambda: self.play_round("rock")
        ).grid(row=0, column=0, padx=4)
        tk.Button(
            button_frame,
            text="Paper",
            width=10,
            command=lambda: self.play_round("paper"),
        ).grid(row=0, column=1, padx=4)
        tk.Button(
            button_frame,
            text="Scissors",
            width=10,
            command=lambda: self.play_round("scissors"),
        ).grid(row=0, column=2, padx=4)

        self.computer_choice_label = tk.Label(
            root, text="Computer chose: -", font=("Segoe UI", 11)
        )
        self.computer_choice_label.pack(pady=6)

        self.result_label = tk.Label(
            root, text="Pick a move to start.", font=("Segoe UI", 11, "bold")
        )
        self.result_label.pack(pady=6)

        self.score_label = tk.Label(
            root,
            text="Score - You: 0  Computer: 0  Ties: 0",
            font=("Segoe UI", 11),
        )
        self.score_label.pack(pady=6)

        controls_frame = tk.Frame(root)
        controls_frame.pack(pady=12)

        tk.Button(
            controls_frame, text="Reset", width=12, command=self.reset_scores
        ).grid(row=0, column=0, padx=6)
        tk.Button(controls_frame, text="Quit", width=12, command=root.destroy).grid(
            row=0, column=1, padx=6
        )

    def play_round(self, player_choice: str) -> None:
        """Play one round, update winner text, and refresh running scores."""
        computer_choice = random.choice(CHOICES)
        self.computer_choice_label.config(text=f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            self.tie_score += 1
            self.result_label.config(text="It is a tie!")
        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "paper" and computer_choice == "rock")
            or (player_choice == "scissors" and computer_choice == "paper")
        ):
            self.player_score += 1
            self.result_label.config(text="You win this round!")
        else:
            self.computer_score += 1
            self.result_label.config(text="Computer wins this round!")

        self.update_score_label()

    def reset_scores(self) -> None:
        """Reset all score counters and refresh display text."""
        self.player_score = 0
        self.computer_score = 0
        self.tie_score = 0
        self.result_label.config(text="Scores reset. Pick a move to start.")
        self.computer_choice_label.config(text="Computer chose: -")
        self.update_score_label()

    def update_score_label(self) -> None:
        """Render the latest score totals on the scoreboard label."""
        self.score_label.config(
            text=(
                f"Score - You: {self.player_score}  "
                f"Computer: {self.computer_score}  "
                f"Ties: {self.tie_score}"
            )
        )


def main() -> None:
    """Create and run the Tkinter application."""
    root = tk.Tk()
    RockPaperScissorsApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

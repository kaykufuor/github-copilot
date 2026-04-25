"""Rock Paper Scissors Lizard Spock game."""

import random


CHOICES = {
    1: "Rock ✊",
    2: "Paper ✋",
    3: "Scissors ✌️",
    4: "Spock 🖖",
    5: "Lizard 🦎",
}

# Each key beats the two values in its set.
WIN_RULES = {
    1: {3, 5},
    2: {1, 4},
    3: {2, 5},
    4: {1, 3},
    5: {2, 4},
}

WIN_MESSAGES = {
    (1, 3): "Rock crushes Scissors.",
    (1, 5): "Rock crushes Lizard.",
    (2, 1): "Paper covers Rock.",
    (2, 4): "Paper disproves Spock.",
    (3, 2): "Scissors cuts Paper.",
    (3, 5): "Scissors decapitates Lizard.",
    (4, 1): "Spock vaporizes Rock.",
    (4, 3): "Spock smashes Scissors.",
    (5, 2): "Lizard eats Paper.",
    (5, 4): "Lizard poisons Spock.",
}


def build_menu() -> str:
    return """ 
===================
Rock Paper Scissors
===================

1) Rock ✊
2) Paper ✋
3) Scissors ✌️
4) Spock 🖖
5) Lizard 🦎
Pick a number: """


def get_player_choice() -> int | None:
    raw_choice = input(build_menu())
    try:
        choice = int(raw_choice)
    except ValueError:
        return None

    if choice in CHOICES:
        return choice
    return None


def get_round_result(player: int, computer: int) -> str:
    if player == computer:
        return "It's a tie!"

    if computer in WIN_RULES[player]:
        detail = WIN_MESSAGES[(player, computer)]
        return f"You win! {detail}"

    detail = WIN_MESSAGES[(computer, player)]
    return f"You lose. {detail}"


def main() -> None:
    player_choice = get_player_choice()
    if player_choice is None:
        print("Invalid input. Please pick a number from 1 to 5.")
        return

    computer_choice = random.randint(1, 5)

    print(f"You chose: {CHOICES[player_choice]}")
    print(f"Computer chose: {CHOICES[computer_choice]}")
    print(get_round_result(player_choice, computer_choice))


if __name__ == "__main__":
    main()

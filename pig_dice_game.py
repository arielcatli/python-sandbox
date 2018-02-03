#PIG Dice game

import random

score = 0
turn = 1
game_over = False
turn_over = False
turn_score = 0

def main():
    print("THIS IS THE PIG DICE GAME!")a
    display_rules()
    play_game()

def display_rules():
    print("* The Pig Dice Game!"
            , "* Roll the die. If you get 1, you lose the turn along with your points."
            , "* If you don't get 1, you have the choice to roll the die again or hold your turn."
            , "* Collect up to 20 points with the fewest turns!",sep="\n")

def play_game():
    print("\n\nLet's play the game!")
    global game_over, score, turn
    while not game_over:
        print(f"\n\nTURN {turn}")
        take_turn()
        print(f"CURRENT SCORE: {score}")
    print(f"\n\nGame over at {turn} turns.")


def take_turn():
    global score, turn_over, turn, turn_score
    turn_score = 0
    turn_over = False
    while not turn_over:
        choice = input("Roll or hold? [R][H] : ").lower()
        if choice == 'r':
            roll_die()
        elif choice == 'h':
            hold_turn()
    turn += 1
    score += turn_score

def roll_die():
    global turn_score, turn_over
    die = random.randint(1,6)
    print(f"DIE: {die}")
    if(die == 1):
        turn_over = True
        print("Your turn is over. You don't get any point from this turn.")
    else:
        turn_score += die
        print(f"Your turn is over. You get {die} points from this turn.")
        turn_over = True

def hold_turn():
    global score, game_over, turn_over
    if score >= 20:
        print(f"You won the game! You score now is {score}.")
        game_over = True
        turn_over = True
    else:
        print("Okay. We will not roll the die. We will proceed to the next turn.")
        turn_over = True


if __name__ == "__main__":
    main()

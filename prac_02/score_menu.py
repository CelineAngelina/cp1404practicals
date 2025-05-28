MENU = "(G)et a valid score\n(P)rint result\n(S)how stars (this should print as many stars as the score)\n(Q)uit"
INVALID_SCORE = -1
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100

def main():
    """Display the menu and perform based on the user's choice."""
    score = INVALID_SCORE
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            if score != INVALID_SCORE:
                result = determine_score(score)
                print(f"Your score of {score} is {result}")
            else:
                print("Please enter a valid score first.")
        elif choice == 'S':
            if score != INVALID_SCORE:
                print_star(score)
            else:
                print("Please enter a valid score first.")
        else:
            print("Invalid option.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")

def get_valid_score():
    """Get a valid score that falls within the range of 0 to 100."""
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def determine_score(score):
    """Determine user's result based on the score."""
    if score < 50:
        return "Bad"
    if score < 90:
        return "Passable"
    return "Excellent"

def print_star(score):
    """Print as many stars as the score."""
    print('*' * int(score))

main()
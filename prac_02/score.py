import random
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100

def main():
    """Get user score and print it result."""
    # score = float(input("Enter score: "))
    score = generate_random_score()
    result = determine_score(score)
    print(f"Your score {score} is {result}")

def generate_random_score():
    """Generate a random score that is in between 0-100."""
    return random.randint(MINIMUM_SCORE,MAXIMUM_SCORE)

def determine_score(score):
    """Determine user's result based on the score."""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    if score < 50:
        return "Bad"
    if score < 90:
        return "Passable"
    return "Excellent"

main()
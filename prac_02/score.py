import random

def main():
    """Get user score and print it result."""
    # score = float(input("Enter score: "))
    score = generate_random_score()
    result = determine_score(score)
    print(f"Your score - {score} is {result}")

def generate_random_score():
    """Generate a random score that is in between 0-100."""
    return random.randint(0,100)

def determine_score(score):
    """Determine user's result based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score < 50:
        return "Bad"
    if score < 90:
        return "Passable"
    return "Excellent"

main()
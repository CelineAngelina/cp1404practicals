def main():
    """Get user score and print it result."""
    score = float(input("Enter score: "))
    result = determine_score(score)
    print(result)

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
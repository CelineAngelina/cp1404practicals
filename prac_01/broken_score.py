"""
CP1404/CP5632 - Practical
Broken program to determine score status

pseudocode:
get score
if score < 0 or score > 100
    display "Invalid score"
else if score < 50
    display "Bad"
else if score < 90
    display "Passable"
else
    display "Excellent"
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score < 50:
    print("Bad")
elif score < 90:
    print("Passable")
else:
    print("Excellent")

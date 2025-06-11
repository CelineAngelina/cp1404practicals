import random

NUMBER_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

quick_pick = int(input("How many quick picks? "))
while quick_pick < 0:
    print("Invalid pick")
    quick_pick = int(input("How many quick picks? "))

for i in range(quick_pick):
    numbers = []
    while len(numbers) < NUMBER_PER_LINE:
        number = random.randint(MINIMUM, MAXIMUM)
        if number not in numbers:
            numbers.append(number)
        numbers.sort()
    print(" ".join((f"{number:2}" for number in numbers)))
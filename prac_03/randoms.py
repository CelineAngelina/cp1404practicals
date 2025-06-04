import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
    # 14, 6, 9, 7, 19, 6
# What was the smallest number you could have seen, what was the largest?
    # The smallest number that I had seen after six tries was 6 and the largest number was 19.

# What did you see on line 2?
    # 3, 7, 7, 9, 5, 7
# What was the smallest number you could have seen, what was the largest?
    # The smallest number among the output was 3 and largest number was 9
# Could line 2 have produced a 4?
    # No, because the code uses a step of 2 starting from 3, so it only prints numbers like 3, 5,7, and 9.
    # Since 4 is not in the sequence, it can never be printed.

# What did you see on line 3?
    # 4.392172220792992, 4.201107450198835, 4.966304069639943, 3.0107908091933284, 4.339879891333248, 3.3989336163146238
# What was the smallest number you could have seen, what was the largest?
    # The smallest number I saw was 3.0107908091933284 and the largest was 4.966304069639943

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 101))
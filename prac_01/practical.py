"""
get number_of_gifts
get number_of_students
number_of_gift_for_each_student = number of gifts // number of students
left_over = number_of_gifts % number_of_students
display number_of_gift_for_each_student and left_over
"""

# number_of_gifts = int(input("number of gifts: "))
# number_of_students = int(input("number of students: "))
# number_of_gift_for_each_student = number_of_gifts // number_of_students
# left_over = number_of_gifts % number_of_students
# print(f"number of gift each student gets is {number_of_gift_for_each_student} and there are {left_over} gift(s) left.")

# item_price = float(input("price of the item: $"))
# gst = input("Is there any GST charges? (yes or no): ").lower()
# if gst == "yes":
#     item_price *= 1.09 # 9%
# print(f"the final price is {item_price:.2f}")

# while loop
# start_number = 0
# end_number = int(input("Enter a number: "))
# while start_number < end_number:
#     start_number += 1
#     print(start_number,end=" ")

# for loop
# end_number = int(input("Enter a number: "))
# for i in range(1, end_number+1):
#     print(i, end=" ")

# SECRET_NUMBER = 5
# guess_number = int(input("Guess a number (1-10): "))
# while guess_number != SECRET_NUMBER:
#     print("wrong:( take a guess again!")
#     guess_number = int(input("Guess a number (1-10): "))
# print("yeay :) you got it!")

# user_name = input("Your name: ").upper()
# while user_name == "":
#     print("Name can't be blank")
#     user_name = input("Your name: ").upper()
#
# salary = float(input("Your salary: $ "))
# while salary < 0:
#     print("The amount can't be lower than $0")
#     salary = float(input("Your salary: $ "))
#
# print(f"{user_name} has ${salary:.2f}")

# total_age = 0
# number_of_ages = int(input("Enter number of ages: "))
# for i in range(number_of_ages):
#     age = int(input(f"Age for person {i+1}: "))
#     total_age += age
#
# average_age = total_age / number_of_ages
# print(f"The total age is {total_age} and the average is {average_age}")
#
# total_age = 0
# count = 0
# age = int(input(f"Age: "))
# while age != -1:
#     total_age += age
#     age = int(input(f"Age: "))
#     count += 1
#
# average_age = total_age / count
# print(f"The total age is {total_age} and the average is {average_age}")

# for i in range(1,4):
#     for j in range(2, 10, 3):
#         print(i, "-", j+i)
"""
123 258
1-3
1-6
1-9
2-4
2-7
2-10
3-5
3-8
3-11
"""

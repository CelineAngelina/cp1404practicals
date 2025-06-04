# FILENAME = "random.txt.txt"
# file_name = open(input("Filename: "), "r")
# for line in file_name:
#     if line.startswith("#"):
#         print(line.strip())
#
# file_name.close()

# with open(FILENAME, "a") as out_file:
#     out_file.write(name)
# #using 'with' does not require us to close the file


# s = "\tPython, Monty \n"
# print(s[1], ".", sep="")
# print(s.strip(), ".", sep="")
# s = s.replace(' ', '*') #replace spaces with asterisk - only spaces
# print(s.lstrip(), ".", sep="")
# print(s.strip().split(',')) #the output will become a list

"""
\t = tab spacing
"""
from tkinter.font import names

"""
name = input("Name: ")
out_file = open("names.txt", "w")
print(name, file=out_file)
out_file.close
print("Done")
"""
# name = input("Name: ")
# with open("names.txt", "w") as out_file:
#     # out_file.write(name)
#     print(name, file=out_file)
# print("Done")

"""
Write code that creates files from a list of strings.
Each file should be named with the value of the string with a .txt extension. 
If the string is "Bob", create a file called "Bob.txt". 
Write the string to the file.

Version 2: 
Write the position in the list to the file, starting from 1.
"""

# names = ["Andy", "Bob", "Cindy"]
# for i in range(len(names)):
#     with open(f"{names[i]}.txt", "w") as out_file:
#         print(f"{i+1}. {names[i]}", file=out_file

# in_file = open("random.txt", "r")
# for line in in_file:
#     name = line.strip()
#     country = in_file.readline().strip()
#     print(f"{name} was born in {country}")
# in_file.close()

# try:
#     print(10/0) #the statement that will possibly crash the program
# except ZeroDivisionError: #tell the Python the error i wanna catch
#     print("Division cannot divide by zero")

# try:
#     in_file = open("abc.txt", "r")
#     print(in_file)
# except FileNotFoundError:
#     print("File does not exist.")

# try:
#     number = int(input("Enter a number: "))
#     print(number)
# except ValueError:
#     print("Input is not a number")
#
# a = "12"
# b = 4
#
# print(a + b)

# try:
#     print(a + b)
# except TypeError:
#     print("Not a valid integer")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i, number in enumerate(numbers, 1):
#     print(f"2 ^{number:2} is {2**number:4}")
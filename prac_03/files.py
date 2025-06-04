# 1.
# FILENAME = "name.txt"
# output_file = open(FILENAME, "w")
# name = input("Enter your name: ")
# print(name, file=output_file)
# output_file.close()

# 2.
# FILENAME = "name.txt"
# output_file = open(FILENAME, 'r')
# name = output_file.read().strip()
# print(f"Hi {name}!")
# output_file.close()

# 3.
FILENAME = "numbers.txt"
with open(FILENAME, 'r') as out_file:
    first_number= int(out_file.readline().strip())
    second_number = int(out_file.readline().strip())
    total = first_number + second_number
    print(total)


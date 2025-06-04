# 1.
# FILENAME = "name.txt"
# output_file = open(FILENAME, "w")
# name = input("Enter your name: ")
# print(name, file=output_file)
# output_file.close()

# 2.
FILENAME = "name.txt"
output_file = open(FILENAME, 'r')
name = output_file.read().strip()
print(f"Hi {name}!")
output_file.close()

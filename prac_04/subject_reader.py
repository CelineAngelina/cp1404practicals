FILENAME = "subject_data.txt"

def main():
    data = load_data()
    print(data)
    print()
    print_subject_details(data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    with open(FILENAME) as input_file:
        lines = input_file.readlines()
        for line in lines:
            print(line)  # See what a line looks like
            print(repr(line))  # See what a line really looks like
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            print(parts)  # See what the parts look like (notice the integer is a string)
            parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
            print(parts)  # See if that worked
            print("----------")
            data.append(parts)
    return data

def print_subject_details(data):
    """Display subject details where each line shows the subject code, lecturer name, and number of students."""
    for i in range(len(data)):
        print(f"{data[i][0]} is taught by {data[i][1]:12} and has {data[i][2]:3} students")

main()
"""
Project Management
Estimate: 2 hours
Actual:
start 11:09
"""

from prac_07.project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
FILENAME = "projects.txt"

def main():
    project_count = 0
    print("Welcome to Pythonic Project Management")
    with open(FILENAME, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            project_count += 1
        print(f"Loaded {project_count} projects from {FILENAME}")
    print(MENU)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_project()
            choice = input(">>> ").upper()
        elif choice == "S":
            break

        elif choice == "D":
            break

        elif choice == "F":
            break

        elif choice == "A":
            break

        elif choice == "U":
            break

        else:
            print("Invalid choice")
            choice = input(">>> ").upper()

    print("Thank you for using custom-built project management software.")


def load_project():
    """Prompt the user for a filename to load projects from and load them."""
    new_filename = input("Enter the filename: ")
    with open(new_filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            percent_complete = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, percent_complete)
            print(project)


main()
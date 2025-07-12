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
            filename = input("Enter the filename: ")
            projects = load_project(filename)
            for project in projects:
                print(project)

        elif choice == "S":
            break

        elif choice == "D":
            projects = load_project(FILENAME)
            incomplete_projects = [incomplete_project for incomplete_project in projects if incomplete_project.completion_percentage < 100]
            completed_projects = [completed_project for completed_project in projects if completed_project.completion_percentage >= 100]

            incomplete_projects.sort()
            print("Incomplete projects:")
            for projects in incomplete_projects:
                print(f"\t{projects}")

            completed_projects.sort()
            print("Completed projects:")
            for projects in completed_projects:
                print(f"\t{projects}")

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


def load_project(prompt):
    """Load projects from the prompt."""
    projects = []
    with open(prompt, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            percent_complete = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, percent_complete)
            projects.append(project)
    return projects


main()

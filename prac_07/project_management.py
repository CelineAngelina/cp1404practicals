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
    """"""
    print("Welcome to Pythonic Project Management")
    projects = load_project(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    print(MENU)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Enter the filename: ")
            projects = load_project(filename)
            display_projects("Projects:", projects)

        elif choice == "S":
            break

        elif choice == "D":
            projects = load_project(FILENAME)
            display_completed_and_incomplete_projects(projects)

        elif choice == "F":
            break

        elif choice == "A":
            break

        elif choice == "U":
            break

        else:
            print("Invalid choice")
        print(MENU)
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


def display_completed_and_incomplete_projects(projects):
    """Display completed and incomplete projects, both sorted by priority."""
    incomplete_projects = [incomplete_project for incomplete_project in projects if
                           incomplete_project.completion_percentage < 100]
    completed_projects = [completed_project for completed_project in projects if
                          completed_project.completion_percentage >= 100]
    incomplete_projects.sort()
    completed_projects.sort()

    display_projects("Incomplete projects:", incomplete_projects)
    display_projects("Completed projects:", completed_projects)


def display_projects(title, projects):
    """Display list of projects with a given title."""
    print(title)
    for projects in projects:
        print(f"\t{projects}")

main()

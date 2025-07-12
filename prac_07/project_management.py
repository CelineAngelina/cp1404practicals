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
            display_projects(projects)

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
            projects = load_project(FILENAME)
            update_project_choice(projects)

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
    print("Incomplete projects:")
    display_projects(incomplete_projects)
    completed_projects.sort()
    print("Complete projects:")
    display_projects(completed_projects)

def display_projects(projects):
    """Display list of projects."""
    for projects in projects:
        print(f"\t{projects}")

def get_valid_project_choice(projects):
    """"""
    project_choice = int(input("Project choice: "))
    while project_choice >= len(projects):
        print("Invalid choice")
        project_choice = int(input("Project choice: "))
    return project_choice

def save_project_details():
    """"""
    with open(FILENAME, 'r') as in_file:
        lines = in_file.readlines()
    header = lines[0]
    project_lines = lines[1:]
    return header, project_lines

def write_updated_project_details(header, project_lines):
    """"""
    with open(FILENAME, 'w') as out_file:
        out_file.write(header)
        out_file.writelines(project_lines)

def update_project_choice(projects):
    """"""
    for i, project in enumerate(projects, start=0):
        print(f"{i} {project}")
    project_choice = get_valid_project_choice(projects)
    selected_project = projects[project_choice]
    print(selected_project)
    new_percentage = input("New Percentage: ")
    if new_percentage:
        selected_project.completion_percentage = int(new_percentage)
    new_priority = input("New Priority: ")
    if new_priority:
        selected_project.priority = int(new_priority)
    header, project_lines = save_project_details()
    project_lines[
        project_choice] = f"{selected_project.name}\t{selected_project.start_date}\t{selected_project.priority}\t{selected_project.cost_estimate}\t{selected_project.completion_percentage}\n"
    write_updated_project_details(header, project_lines)

main()

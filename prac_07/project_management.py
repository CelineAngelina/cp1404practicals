"""
Project Management
Estimate: 2 hours
Actual:
start 11:09
"""

from prac_07.project import Project
import datetime

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
            save_filename = input("Enter filename to save projects: ")
            with open(save_filename, 'w') as out_file:
                out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
                for project in projects:
                    out_file.write(
                        f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")

        elif choice == "D":
            projects = load_project(FILENAME)
            display_completed_and_incomplete_projects(projects)
        elif choice == "F":
            projects = load_project(FILENAME)
            filter_project(projects)
        elif choice == "A":
            print("Let's add a new project")
            add_new_project()
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

def update_project_choice(projects):
    """Allow the user to select a project and update its percentage and/or priority."""
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

def get_valid_project_choice(projects):
    """Prompt valid project choice from user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            project_choice = int(input("Project choice: "))
            if project_choice >= len(projects):
                print("Invalid choice")
            else:
                is_valid_input = True
                return project_choice
        except ValueError:
            print("Invalid input; enter a valid number")

def save_project_details():
    """Load all project details from the file into memory before updating."""
    with open(FILENAME, 'r') as in_file:
        lines = in_file.readlines()
    header = lines[0]
    project_lines = lines[1:]
    return header, project_lines

def write_updated_project_details(header, project_lines):
    """Overwrite the file with the header and updated project details."""
    with open(FILENAME, 'w') as out_file:
        out_file.write(header)
        out_file.writelines(project_lines)

def get_new_project_details():
    """Get new project details from the user and return a Project instance."""
    new_project_name = input("Name: ").title()
    new_project_start_date = input("Start date (dd/mm/yy): ")
    new_project_priority = int(input("Priority: "))
    new_project_cost_estimate = float(input("Cost estimate: $"))
    new_project_percentage_complete = int(input("Percent complete: "))
    return Project(new_project_name, new_project_start_date, new_project_priority, new_project_cost_estimate, new_project_percentage_complete)

def add_new_project():
    """Prompt user for a new project and append it to the projects file."""
    new_project = get_new_project_details()
    with open(FILENAME, 'a') as out_file:
        out_file.write(
            f"{new_project.name}\t{new_project.start_date}\t{new_project.priority}\t{new_project.cost_estimate}\t{new_project.completion_percentage}\n")

def filter_project(projects):
    """Filter and display only the projects that start on or after the date the user enters."""
    project_after_date = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(project_after_date, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if
                         datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() >= filter_date]
    filtered_projects.sort()
    display_projects(filtered_projects)

main()

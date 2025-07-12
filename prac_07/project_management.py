"""
Project Management
Estimate: 2 hours
Actual:
start 11:09
"""


MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
FILENAME = "projects.txt"

def main():
    print("Welcome to Pythonic Project Management")
    in_file = open(FILENAME, 'r')
    in_file.readline()
    project_count = 0
    for line in in_file:
        project_count += 1
    in_file.close()
    print(f"Loaded {project_count} projects from {FILENAME}")
    print(MENU)

main()
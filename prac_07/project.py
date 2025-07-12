class Project:
    """Represent a Project with name, start date, priority, cost estimation, and completion percentage."""
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion_percentage=0):
        """Initialise a Project instance"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of the project."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Compare one project to another by priority."""
        return self.priority < other.priority


# def run_test():
#     project1 = Project("Build Car Park", "12/09/2021", 2, 600000, 95)
#     project2 = Project("Organise Pantry", "20/07/2022", 1, 25, 55)
#     project3 = Project("Record Music Video", "01/12/2022", 9, 250000, 0)
#
#     projects = [project1, project2, project3]
#
#     projects.sort()
#     for project in projects:
#         print(project)
#
# if __name__ == "__main__":
#     run_test()
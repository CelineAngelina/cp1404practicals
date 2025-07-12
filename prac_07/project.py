class Project:
    """"""
    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion_percentage=0):
        """"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"


def run_test():
    test1 = Project("Organise Pantry", "20/07/2022", 1, 25, 55)

    print(test1)

if __name__ == "__main__":
    run_test()
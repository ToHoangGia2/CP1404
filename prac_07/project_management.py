import datetime
from project import Project

FILENAME = "projects.txt"

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""

def main():
    """a"""
    print("Welcome to Pythonic Project Management")
    load_projects()
    print(MENU)
    user_input = input(">>> ").upper()
    while user_input != "Q":
        if user_input == "L":
            load_projects()
        elif user_input == "S":
            #TODO save project
            print("\n WORK IN PROGRESS")

        elif user_input == "D":
            #TODO display project
            print("\n WORK IN PROGRESS")

        elif user_input == "F":
            #TODO display filter
            print("\n WORK IN PROGRESS")

        elif user_input == "A":
            #TODO display add new proj
            print("\n WORK IN PROGRESS")

        elif user_input == "U":
            #TODO display update
            print("\n WORK IN PROGRESS")

        else:
            print("Invalid input")
        user_input = input(">>> ").upper()

    #TODO save project
    print("Thank you for using custom-built project management software.")


def load_projects():
    projects = []
    projects_loaded = 0
    with open(FILENAME,"r") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project_name = parts[0]
            project_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            project_priority = int(parts[2])
            project_cost_estimate = float(parts[3])
            project_completion_percentage = int(parts[4])
            project = Project(project_name, project_date, project_priority, project_cost_estimate, project_completion_percentage)
            projects.append(project)
            projects_loaded += 1
    print(f"Loaded {projects_loaded} projects from {FILENAME}.")
    return projects


main()

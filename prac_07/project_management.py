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
    projects = load_projects()
    print(MENU)
    user_input = input(">>> ").upper()
    while user_input != "Q":
        if user_input == "L":
            projects = load_projects()

        elif user_input == "S":
            save_projects(projects)
            print("saved projects successfully")

        elif user_input == "D":
            display_projects(projects)


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

    save_or_not = input("Would you like to save to projects.txt?").upper()
    if save_or_not == "Y":
        save_projects(projects)
    print("Thank you for using custom-built project management software.")


def load_projects():
    """load projects to a list then return it"""
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

def save_projects(projects):
    """save projects to txt file"""
    with open(FILENAME,"w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date:%d/%m/%Y}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)

def display_projects(projects):
    """display projects by date"""
    not_complete, completed = sort_complete(projects)
    print(not_complete)
    print(completed)


def sort_complete(projects):
    not_complete = []
    completed = []
    for project in projects:
        if project.is_complete():
            completed.append(project)
        else:
            not_complete.append(project)
    return(not_complete, completed)


main()

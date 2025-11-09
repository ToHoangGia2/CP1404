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
            filtered_dates = filter_dates(projects)
            for date in filtered_dates:
                print(date)

        elif user_input == "A":
            print("Let's add a new project")
            project = create_new_project()
            projects.append(project)

        elif user_input == "U":
            #TODO display update
            print("\n WORK IN PROGRESS")

        else:
            print("Invalid input")

        print(MENU)
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
    projects.sort()
    not_complete, completed = determine_complete(projects)
    print("Incomplete projects:")
    for project in not_complete:
        print(project)
    print("Completed projects:")
    for project in completed:
        print(project)



def determine_complete(projects):
    not_complete = []
    completed = []
    for project in projects:
        if project.is_complete():
            completed.append(project)
        else:
            not_complete.append(project)
    return(not_complete, completed)

def create_new_project():
    """create a new project"""
    project_name = input("Name: ")
    date = get_valid_date("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost Estimate:"))
    completion_percentage = int(input("Completion Percentage:"))
    project = Project(project_name, date, priority, cost_estimate, completion_percentage)
    return project


def get_valid_date(Text):
    """get a valid date with input text"""
    while True:
        try:
            date_string = input(Text).strip()
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            return date
        except ValueError:
            print("Invalid date")

def filter_dates(projects):
    """filter projects by date"""
    filtered_projects = []
    filter_date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
    projects.sort()
    for project in projects:
        if project.start_date >= filter_date:
            filtered_projects.append(project)
    return filtered_projects

main()

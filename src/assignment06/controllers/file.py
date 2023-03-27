import os

from models import csv as c

LOCATION_PROMPT = "Give the location and name of the database file that is relative to the above path (e.g. /folder/hr.csv):\n>>>"
SEPARATOR = "---------------------"
NEW_LINE_PROMPT = "\n>>>"

def get_current_folder():
    return os.getcwd()

def is_file(path):
    return os.path.isfile(path)

def get_file_path(prompt):
    while True: 
        print(SEPARATOR)
        path = f"{get_current_folder()}\\resources\\hr.csv"
        print(f"The current path is:\n{path}")
        print(SEPARATOR)         
        decision = input(f"Is the path correct? Confirm with [Y] or change with [N]:{NEW_LINE_PROMPT}")  
        if decision.upper() == 'N':
            path = input("Enter the path:")
        elif decision.upper() == 'Y':
            break
        else:
            print("[Y] or [N] are acceptable options.") 
        if is_file(path):
            break
        else:
            print("The file doesn't exist.")
            continue
    return path

def get_csv_content(path):
    with open(path, 'r') as file:
        return file.readlines()

def get_csv():
    path = get_file_path(LOCATION_PROMPT)
    content = get_csv_content(path)
    header = content[:1]
    value = content[1:]
    csv = c.Csv(path, header, value)
    return csv

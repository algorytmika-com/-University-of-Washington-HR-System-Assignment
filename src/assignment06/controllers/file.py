import os

from models import csv as c
from utils import format as f
import csv



def get_current_folder():
    return os.getcwd()

def is_file(path):
    return os.path.isfile(path)

def get_file_path(prompt):
    while True: 
        path = f"{get_current_folder()}\\resources\\hr.csv"
        f.print_message(f"The current path is:\n{path}")
    
        decision = input(f"Is the path correct? Confirm with [Y] or change with [N]:{f.NEW_LINE_PROMPT}")  
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
    
def save_csv_to_file(path, content):
    with open(path, 'w') as file:
        file.write(content)

def get_csv():
    path = get_file_path(f.LOCATION_PROMPT)
    content = get_csv_content(path)
    header = content[:1]
    values = content[1:]
    csv = c.Csv(path, header, values)
    return csv






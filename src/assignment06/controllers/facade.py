import sys, os

from controllers import file as f, employment as e
from utils import format as fmt

csv = None
employee_dict = {}

prompt = "\n".join(("Please choose from below options:",
          "1 - Load employees in from a file",
          "2 - Save employees into a file",
          "3 - Add a new employee",
          "4 - Generate a report of current employees",
          "5 - Generate a report of employees who have recently left",
          "6 - Generate a report of annual review reminders",
          "7 - Quit",
          ">>> "))

def load_employees():
    global csv
    csv = f.get_csv()
    global employee_dict
    employee_dict = e.get_employee_dict(csv)
    print(fmt.print_message("Employees are loaded in from file."))

def save_employees():
    new_path = f.get_file_path(fmt.LOCATION_PROMPT)
    employee_content #todo
    f.save_csv(employee_dict, csv, new_path)

def add_employee():
    pass

def report_current_employees():
    pass

def report_former_employees():
    pass

def report_reminders():
    pass

def exit_program():
    print("Bye!")
    sys.exit() 

def clear_console():
    clear = lambda: os.system('cls')
    clear()
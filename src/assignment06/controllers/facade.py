import sys, os

from controllers import file as f


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
    csv = f.get_csv()
    print(csv.path)
    print(csv.header)
    print(csv.value)

def save_employees():
    pass

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
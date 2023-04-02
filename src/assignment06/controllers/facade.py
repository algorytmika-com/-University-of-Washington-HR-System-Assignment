import sys, os

from controllers import file as f, employment as e, report as r
from utils import format as fmt

#is_file_loaded = False
#csv = None
#employee_dict = {}

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
    global employee_dict
    global is_file_loaded
    csv = f.get_csv()
    employee_dict = e.get_employee_dict(csv)
    is_file_loaded = True
    fmt.print_message("Employees are loaded in from file.")

def save_employees():
    new_path = f.get_file_path(fmt.LOCATION_PROMPT)
    employee_content = e.get_employee_content(csv.header, employee_dict)
    f.save_csv_to_file(new_path, employee_content)
    fmt.print_message("Employees saved to a file.")

def add_employee():
    global employee_dict
    employee_id = e.get_employee_incremented_id(employee_dict)
    name = e.get_input_employee_name()
    address = e.get_input_employee_address()
    ssn = e.get_input_employee_ssn()
    date_of_birth = e.get_input_employee_date_of_birth()
    job_title = e.get_input_employee_job_title()
    start_date = e.get_input_employee_start_date()
    end_date = e.get_input_employee_end_date()
    employee_obj = e.get_employee_obj(employee_id, name, address, ssn, date_of_birth,
                                      job_title, start_date, end_date)
    employee_dict[employee_id] = employee_obj
    fmt.print_message("Employee added to memory. Use option 2 to save to a file.")  

def report_current_employees():
    print(fmt.print_message("CURRENT EMPLOYEES")) 
    r.print_current_employees(employee_dict)

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
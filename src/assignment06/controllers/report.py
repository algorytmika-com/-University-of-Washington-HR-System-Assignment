from models import employee as e
from utils  import date_utils as d


def print_current_employees(employee_dict):
    current_employee_dict = {}
    for e in employee_dict.values():
        if not e.end_date:
            current_employee_dict[e.employee_id] = e
    print_employees(current_employee_dict)

def print_former_employees(employee_dict, up_to_days_ago):
    former_employee_dict = {}
    for e in employee_dict.values():
        if e.end_date:
            try:
                end_date = d.get_date_converted_from_str(e.end_date, '%m/%d/%Y')
            except ValueError:
                print("End date is not formatted as mm/dd/YYYY")
                break
            if d.is_date_in_past_days(end_date, up_to_days_ago):
                former_employee_dict[e.employee_id] = e
    print_employees(former_employee_dict)

def print_annual_review_reminder(employee_dict, days_wtihin):
    annual_employee_dict = {}
    for e in employee_dict.values():
        if not e.end_date:
            try:
                start_date = d.get_date_converted_from_str(e.start_date, '%m/%d/%Y')
            except ValueError:
                print("Start date is not formatted as mm/dd/YYYY")
                break
            next_anniversary = d.get_next_anniversary(start_date)
            if d.is_date_in_future_days(next_anniversary, days_wtihin):
                annual_employee_dict[e.employee_id] = e
    print_employees(annual_employee_dict)


def print_employees(employee_dict):
    print(get_formatted_employee('Full Name','Address','SSN','Birth Date','Job Title','Start Date','End Date'))
    print_underline()
    for emp in employee_dict.values():
        print(get_formatted_employee(emp.name, emp.address, emp.ssn, emp.date_of_birth, emp.job_title, emp.start_date, emp.end_date))
    print_underline()        

def print_underline():
    print(get_formatted_employee(e.Employee.name_max_length * '-', e.Employee.address_max_length * '-', e.Employee.ssn_max_length * '-', 
                                 e.Employee.date_max_length * '-', e.Employee.job_title_max_length * '-', e.Employee.date_max_length * '-', 
                                 e.Employee.date_max_length * '-'))

def get_formatted_employee(name, address, ssn, date_of_birth, job_title, start_date, end_date):
    separator = ' | '
    formatted_employee = f"{separator.lstrip()}{name:{e.Employee.name_max_length}}{separator}" \
              f"{address:{e.Employee.address_max_length}}{separator}" \
              f"{ssn:{e.Employee.ssn_max_length}}{separator}" \
              f"{date_of_birth:{e.Employee.date_max_length}}{separator}" \
              f"{job_title:{e.Employee.job_title_max_length}}{separator}" \
              f"{start_date:{e.Employee.date_max_length}}{separator}" \
              f"{end_date:{e.Employee.date_max_length}}{separator.rstrip()}"
    return formatted_employee
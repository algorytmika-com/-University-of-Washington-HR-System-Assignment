from models import employee as e


def print_current_employees(employee_dict):
    separator = ' | '
    for e in employee_dict.values():
        print(get_formatted_employee(e.name, e.address, e.ssn, e.date_of_birth, e.job_title, e.start_date, e.end_date))
        
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


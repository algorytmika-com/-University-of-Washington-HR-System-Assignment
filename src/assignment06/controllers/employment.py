from models import employee as e

def get_employee_dict(csv):
    employee_dict = {}
    for employee_row in csv.values:
        employee_list = employee_row.strip().split(',')
        employee_id = employee_list[0].strip()
        name = employee_list[1].strip()
        address = employee_list[2].strip()
        ssn = employee_list[3].strip()
        date_of_birth = employee_list[4].strip()
        job_title = employee_list[5].strip()
        start_date = employee_list[6].strip()
        end_date = employee_list[7] .strip()
        employee = e.Employee(employee_id,name,address,ssn,date_of_birth,job_title,start_date,end_date)
        employee_dict[employee.employee_id] = employee
    return employee_dict


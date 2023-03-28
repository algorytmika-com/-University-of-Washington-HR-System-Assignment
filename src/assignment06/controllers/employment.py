from src.assignment06.models import employee as e

def get_employee_dict(csv):
    employee_dict = {}
    for employee_row in csv.values:
        employee_list = employee_row.strip().split(',')
        employee_id = employee_list[0]
        name = employee_list[1]
        address = employee_list[2]
        ssn = employee_list[3]
        date_of_birth = employee_list[4]
        job_title = employee_list[5]
        start_date = employee_list[6]
        end_date = employee_list[7] 
        employee = e.Employee(employee_id,name,address,ssn,date_of_birth,job_title,start_date,end_date)
        employee_dict[employee.employee_id] = employee
    return employee_dict

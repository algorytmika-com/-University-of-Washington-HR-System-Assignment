from src.assignment06.models import csv as c
from src.assignment06.controllers import employment as e

def test_get_employee_dict_pass():
    header = 'employee_id,name,address,ssn,date_of_birth,job_title,start_date,end_date'
    values = ['7, Anubhaw Arya,Seattle,1234567890,1/1/1970,lecturer,1/1/2021,']
    csv = c.Csv(None, header, values)
    employee_dict = e.get_employee_dict(csv)
    employee = employee_dict['7']
    assert employee.employee_id == '7'
    assert employee.ssn == '1234567890'


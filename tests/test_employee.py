from src.assignment06.models import employee as e

def test_employee_pass():
    employee_name = 'Michael Jordan'
    employee = e.Employee(employee_id=None,name=employee_name,address='address',ssn='ssn',
                          date_of_birth=None, job_title='job',start_date=None,end_date=None)
    assert employee.name == employee_name

class Employee:
    name_max_length = 0
    address_max_length = 0
    ssn_max_length = 11
    job_title_max_length = 0
    date_max_length = 10

    def __init__(self, employee_id,name,address,ssn,date_of_birth,job_title,start_date,end_date):
        self.employee_id = employee_id
        self.name = name
        self.address = address
        self.ssn = ssn
        self.date_of_birth = date_of_birth
        self.job_title = job_title
        self.start_date = start_date
        self.end_date = end_date

        Employee.set_name_max_length(name)
        Employee.set_address_max_length(address)
        Employee.set_job_title_max_length(job_title)

    def set_name_max_length(name):
        if Employee.name_max_length < len(name):
            Employee.name_max_length = len(name)

    def set_address_max_length(address):
        if Employee.address_max_length < len(address):
            Employee.address_max_length = len(address)

    def set_job_title_max_length(job_title):
        if Employee.job_title_max_length < len(job_title):
            Employee.job_title_max_length = len(job_title)            
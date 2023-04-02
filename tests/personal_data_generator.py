from faker import Faker
import pandas as pd
import os

fake = Faker()

df = pd.DataFrame(
    [
        {
            "employee_id" : fake.random_number(digits=3),
            "name": fake.name(),
            "address": fake.city(),
            "ssn" : fake.ssn(),
            "date_of_birth": fake.date('%m/%d/%Y'),
            "job_title": fake.job(),
            "start_date": fake.date('%m/%d/%Y'),
            "end_date" : fake.date('%m/%d/%Y')
        }
        for _ in range(100)
    ]
)

df.to_csv(os.path.dirname(os.path.abspath(__file__)) + "\\..\\resources\\hr.csv", index=False)
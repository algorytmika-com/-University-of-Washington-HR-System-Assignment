from cerberus import Validator
from datetime import datetime

def is_valid(value, option):
    if option == 'full_name':
        return is_full_name(value)
    elif option == 'address':
        return is_address(value)  
    elif option == 'ssn':
        return is_ssn(value)          
    elif option == 'date_of_birth':
        return is_date(value)          
    else:
        return False
    
def is_full_name(input):
    schema = {'input': {'type' : 'string', 'minlength': 5, 'regex' : r'[a-zA-Z \.]+'}}
    v = Validator(schema)
    document = {'input' : input}
    return v.validate(document)

def is_address(input):
    schema = {'input': {'type' : 'string', 'minlength': 5, 'regex' : r'[a-zA-Z ]+'}}
    v = Validator(schema)
    document = {'input' : input}
    return v.validate(document)

def is_ssn(input):
    schema = {'input': {'type' : 'string', 'minlength': 9, 'maxlength': 9, 'regex' : '^[0-9]*$'}}
    v = Validator(schema)
    document = {'input' : input}
    return v.validate(document)

def is_date(input):
    print(000000)
    if isinstance(input, str):
        format_str = '%m/%d/%Y'
        try:
            input = datetime.strptime(input, format_str)
        except ValueError:
            return False
    else:
        return False
    schema = {'input': {'type' : 'datetime'}}
    v = Validator(schema)
    document = {'input' : input}
    return v.validate(document)
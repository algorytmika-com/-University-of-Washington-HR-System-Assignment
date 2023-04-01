from cerberus import Validator

def is_valid(value, option):
    if option == 'full_name':
        return is_full_name(value)
    else:
        return False
    
def is_full_name(input):
    schema = {'input': {'type' : 'string', 'minlength': 5, 'regex' : r'[a-zA-Z \.]+'}}
    v = Validator(schema)
    document = {'input' : input}
    return v.validate(document)

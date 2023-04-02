from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def get_next_anniversary(checked_date):
    years_delta = datetime.today().year - checked_date.year
    anniversary_date = checked_date + relativedelta(years= years_delta)
    if anniversary_date < datetime.today():
        anniversary_date += relativedelta(years= 1)
    return anniversary_date
        
def is_date_in_future_days(checked_date, days):
    if checked_date < datetime.today() or days < 0:
        return False
    future_date = datetime.today() + timedelta(days = days)
    if(checked_date <= future_date):
        return True
    return False

def is_date_in_past_days(checked_date, days):
    if checked_date > datetime.today() or days < 0:
        return False
    past_date = datetime.today() - timedelta(days = days)
    if(checked_date >= past_date):
        return True
    return False

def get_date_converted_from_str(date_str, format):
    return datetime.strptime(date_str, format)
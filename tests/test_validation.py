from src.assignment06.utils import validation as v
from datetime import datetime

def test_is_date_pass():
    date_str = '12/29/2017'
    assert v.is_required_date(date_str)

def test_is_date_fail():
    date_str = '1a/29/2017'
    assert not v.is_required_date(date_str)

def test_is_date_is_future_fail():
    date_str = '11/29/2030'
    assert not v.is_required_date(date_str)    
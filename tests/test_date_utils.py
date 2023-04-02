from src.assignment06.utils import date_utils as d
from datetime import datetime

def test_get_next_anniversary_current_year_pass():
    start_date = datetime(2016, 12, 12)
    expected =   datetime(2023, 12, 12)
    compare_date = datetime(2023, 4, 2)
    actual = d.get_next_anniversary(start_date, compare_date=compare_date)
    assert expected == actual

def test_get_next_anniversary_next_year_pass():
    start_date = datetime(2016, 1, 1)
    expected =   datetime(2024, 1, 1)
    compare_date = datetime(2023, 4, 2)
    actual = d.get_next_anniversary(start_date, compare_date=compare_date)
    assert expected == actual

def test_get_next_anniversary_leap_year_pass():
    start_date = datetime(2016, 2, 29) #leap year
    compare_date = datetime(2022, 4, 2)
    expected =   datetime(2023, 2, 28)
    actual = d.get_next_anniversary(start_date, compare_date=compare_date)
    assert expected == actual

def test_get_next_anniversary_current_year_fail():
    start_date = datetime(2016, 12, 12)
    expected =   datetime(2023, 1, 1)
    compare_date = datetime(2023, 4, 2)
    actual = d.get_next_anniversary(start_date, compare_date=compare_date)
    assert not expected == actual

def test_is_date_in_future_days_pass():
    start_date = datetime(2023, 4, 20)
    compare_date = datetime(2023, 4, 2)    
    actual = d.is_date_in_future_days(start_date, 30)
    assert actual

def test_is_date_in_future_days_fail():
    start_date = datetime(2024, 4, 20)
    compare_date = datetime(2023, 4, 2)    
    actual = d.is_date_in_future_days(start_date, 30)
    assert not actual    

def test_is_date_in_past_days_pass():
    start_date = datetime(2023, 3, 20)
    compare_date = datetime(2023, 4, 2)    
    actual = d.is_date_in_past_days(start_date, 30)
    assert actual    

def test_is_date_in_past_days_fail():
    start_date = datetime(2020, 3, 20)
    compare_date = datetime(2023, 4, 2)    
    actual = d.is_date_in_past_days(start_date, 30)
    assert not actual      
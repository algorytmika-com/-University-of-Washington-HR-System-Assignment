from src.assignment06.models import csv as c

def test_csv_pass():
    path = "path_value"
    header = ['header1', 'header2']
    values = ['value1, values2']
    csv = c.Csv(path, header, values)
    assert csv.path == path
    assert csv.header == header
    assert csv.values == values

"""
    Dummy conftest.py for assignment06.

    If you don't know what this is for, just leave it empty.
    Read more about conftest.py under:
    - https://docs.pytest.org/en/stable/fixture.html
    - https://docs.pytest.org/en/stable/writing_plugins.html
"""

import pytest, sys, os

#set enviroment ot recognize modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '\\..\\src\\assignment06')

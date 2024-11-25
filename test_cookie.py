import pytest
from dessert import Cookie

def test_cookie_calculate_cost():
    cookie = Cookie("Chocolate Chip", 6, 3.99)
    assert cookie.calculate_cost() == 2.00

def test_cookie_calculate_tax():
    cookie = Cookie("Chocolate Chip", 6, 3.99)
    assert cookie.calculate_tax() == 0.14
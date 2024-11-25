import pytest
from dessert import Candy, Cookie, IceCream, Sundae

def test_tax_percent():
    candy = Candy("Candy Corn", 1.5, 0.25)
    assert candy.tax_percent == 7.25

def test_calculate_tax():
    candy = Candy("Candy Corn", 1.5, 0.25)
    assert candy.calculate_tax() == 0.03
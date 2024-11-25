import pytest
from dessert import Sundae

def test_sundae_calculate_cost():
    sundae = Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29)
    assert sundae.calculate_cost() == 3.36

def test_sundae_calculate_tax():
    sundae = Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29)
    assert sundae.calculate_tax() == 0.24
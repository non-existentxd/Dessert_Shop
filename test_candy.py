from dessert import Candy

def test_candy_calculate_cost():
    candy = Candy("Gummy Bears", 0.5, 0.30)
    assert candy.calculate_cost() == 0.15

def test_candy_calculate_tax():
    candy = Candy("Gummy Bears", 0.5, 0.30)
    assert candy.calculate_tax() == 0.01
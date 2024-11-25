from dessert import IceCream

def test_icecream_calculate_cost():
    icecream = IceCream("Pistachio", 2, 0.79)
    assert icecream.calculate_cost() == 1.58

def test_icecream_calculate_tax():
    icecream = IceCream("Pistachio", 2, 0.79)
    assert icecream.calculate_tax() == 0.11
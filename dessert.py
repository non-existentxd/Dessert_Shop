from abc import ABC, abstractmethod
from packaging import Packaging 

class Dessert(ABC, Packaging): 
    def __init__(self, name, quantity, price_per_unit, tax_percent=7.25, packaging=None):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.tax_percent = tax_percent
        self.packaging = packaging  

    @abstractmethod
    def calculate_cost(self):
        pass

    def calculate_tax(self):
        return self.calculate_cost() * (self.tax_percent / 100)

    @abstractmethod
    def __str__(self):
        pass


class Candy(Dessert):
    def __init__(self, name, quantity, price_per_unit, tax_percent=7.25, packaging="Bag"):
        super().__init__(name, quantity, price_per_unit, tax_percent, packaging)

    def calculate_cost(self):
        return self.quantity * self.price_per_unit

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name} ({self.packaging})\n      {self.quantity} lbs. @ ${self.price_per_unit:.2f}/lb.: {cost:.2f}           [Tax: ${tax:.2f}]"


class Cookie(Dessert):
    def __init__(self, name, quantity, price_per_unit, tax_percent=7.25, packaging="Box"):
        super().__init__(name, quantity, price_per_unit, tax_percent, packaging)

    def calculate_cost(self):
        return (self.quantity / 12) * self.price_per_unit  

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name} ({self.packaging})\n      {self.quantity} cookies @ ${self.price_per_unit:.2f}/dozen: {cost:.2f}           [Tax: ${tax:.2f}]"


class IceCream(Dessert):
    def __init__(self, name, quantity, price_per_unit, tax_percent=7.25, packaging="Bowl"):
        super().__init__(name, quantity, price_per_unit, tax_percent, packaging)

    def calculate_cost(self):
        return self.quantity * self.price_per_unit

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name} ({self.packaging})\n      {self.quantity} scoops @ ${self.price_per_unit:.2f}/scoop: {cost:.2f}           [Tax: ${tax:.2f}]"


class Sundae(IceCream):
    def __init__(self, name, quantity, price_per_unit, topping_name, topping_price, tax_percent=7.25, packaging="Boat"):
        super().__init__(name, quantity, price_per_unit, tax_percent, packaging)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        return super().calculate_cost() + self.topping_price

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.topping_name} {self.name} Sundae ({self.packaging})\n      {self.quantity} scoops of {self.name} ice cream @ ${self.price_per_unit:.2f}/scoop\n      {self.topping_name} topping @ ${self.topping_price:.2f}: {cost:.2f}           [Tax: ${tax:.2f}]"
from abc import ABC, abstractmethod

class Dessert(ABC):
    def __init__(self, name, quantity, price_per_unit):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    @abstractmethod
    def calculate_cost(self):
        pass

    def calculate_tax(self):
        return self.calculate_cost() * 0.07

    @abstractmethod
    def __str__(self):
        pass


class Candy(Dessert):
    def __init__(self, name, quantity, price_per_unit):
        super().__init__(name, quantity, price_per_unit)

    def calculate_cost(self):
        return self.quantity * self.price_per_unit

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name}, {self.quantity}lbs, ${self.price_per_unit:.2f}/lb, ${cost:.2f}, ${tax:.2f}"


class Cookie(Dessert):
    def __init__(self, name, quantity, price_per_unit):
        super().__init__(name, quantity, price_per_unit)

    def calculate_cost(self):
        return (self.quantity / 12) * self.price_per_unit  # Assume price per dozen

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name}, {self.quantity} cookies, ${self.price_per_unit:.2f}/dozen, ${cost:.2f}, ${tax:.2f}"


class IceCream(Dessert):
    def __init__(self, name, quantity, price_per_unit):
        super().__init__(name, quantity, price_per_unit)

    def calculate_cost(self):
        return self.quantity * self.price_per_unit

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name}, {self.quantity} scoops, ${self.price_per_unit:.2f}/scoop, ${cost:.2f}, ${tax:.2f}"


class Sundae(IceCream):
    def __init__(self, name, quantity, price_per_unit, topping_name, topping_price):
        super().__init__(name, quantity, price_per_unit)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        return super().calculate_cost() + self.topping_price

    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.topping_name} {self.name} Sundae, {self.quantity} scoops, ${self.price_per_unit:.2f}/scoop, ${cost:.2f}, ${tax:.2f}"
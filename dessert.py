from abc import ABC, abstractmethod


class DessertItem(ABC):
    tax_percent = 7.25

    def __init__(self, name: str = ''):
        self.name = name

    @abstractmethod
    def calculate_cost(self) -> float:
        pass

    def calculate_tax(self) -> float:
        return round(self.calculate_cost() * (self.tax_percent / 100), 2)


class Candy(DessertItem):
    def __init__(self, name: str, candy_weight: float = 0.0, price_per_pound: float = 0.0):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def calculate_cost(self) -> float:
        return round(self.candy_weight * self.price_per_pound, 2)


class Cookie(DessertItem):
    def __init__(self, name: str, cookie_quantity: int = 0, price_per_dozen: float = 0.0):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def calculate_cost(self) -> float:
        return round((self.cookie_quantity / 12) * self.price_per_dozen, 2)


class IceCream(DessertItem):
    def __init__(self, name: str, scoop_count: int = 0, price_per_scoop: float = 0.0):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

    def calculate_cost(self) -> float:
        return round(self.scoop_count * self.price_per_scoop, 2)


class Sundae(IceCream):
    def __init__(self, name: str, scoop_count: int = 0, price_per_scoop: float = 0.0,
                 topping_name: str = '', topping_price: float = 0.0):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self) -> float:
        return round(super().calculate_cost() + self.topping_price, 2)


class Order:
    def __init__(self):
        self.order = []

    def add(self, item: DessertItem):
        self.order.append(item)
    

    def __len__(self):
        return len(self.order)

    def order_cost(self) -> float:
        return round(sum(item.calculate_cost() for item in self.order), 2)

    def order_tax(self) -> float:
        return round(sum(item.calculate_tax() for item in self.order), 2)

from packaging import Packaging

class DessertItem(Packaging):
    def __init__(self, name: str):
        self.name = name
        self.packaging = None  # Default value


class Candy(DessertItem):
    def __init__(self, name: str, weight: float, price_per_lb: float):
        super().__init__(name)
        self.weight = weight
        self.price_per_lb = price_per_lb
        self.packaging = "Bag"

    def __str__(self):
        cost = self.weight * self.price_per_lb
        tax = cost * 0.07
        return (f"{self.name} ({self.packaging})\n"
                f"      {self.weight:.2f} lbs. @ ${self.price_per_lb:.2f}/lb.: "
                f"${cost:.2f}           [Tax: ${tax:.2f}]")



class Cookie(DessertItem):
    def __init__(self, name: str, quantity: int, price_per_dozen: float):
        super().__init__(name)
        self.quantity = quantity
        self.price_per_dozen = price_per_dozen
        self.packaging = "Box"

    def __str__(self):
        cost = (self.quantity / 12) * self.price_per_dozen
        tax = cost * 0.07
        return (f"{self.name} ({self.packaging})\n"
                f"      {self.quantity} cookies @ ${self.price_per_dozen:.2f}/dozen: "
                f"${cost:.2f}           [Tax: ${tax:.2f}]")


class IceCream(DessertItem):
    def __init__(self, name: str, scoops: int, price_per_scoop: float):
        super().__init__(name)
        self.scoops = scoops
        self.price_per_scoop = price_per_scoop
        self.packaging = "Bowl"

    def __str__(self):
        cost = self.scoops * self.price_per_scoop
        tax = cost * 0.07
        return (f"{self.name} ({self.packaging})\n"
                f"      {self.scoops} scoops @ ${self.price_per_scoop:.2f}/scoop: "
                f"${cost:.2f}           [Tax: ${tax:.2f}]")


class Sundae(IceCream):
    def __init__(self, name: str, scoops: int, price_per_scoop: float, topping: str, topping_price: float):
        super().__init__(name, scoops, price_per_scoop)
        self.topping = topping
        self.topping_price = topping_price
        self.packaging = "Boat"

    def __str__(self):
        ice_cream_cost = self.scoops * self.price_per_scoop
        total_cost = ice_cream_cost + self.topping_price
        tax = total_cost * 0.07
        return (f"{self.name} ({self.packaging})\n"
                f"      {self.scoops} scoops of {self.name} ice cream @ ${self.price_per_scoop:.2f}/scoop\n"
                f"      {self.topping} topping @ ${self.topping_price:.2f}: "
                f"${total_cost:.2f}           [Tax: ${tax:.2f}]")

class Order:
    def __init__(self):
        self.items = []

    def add(self, item: DessertItem):
        self.items.append(item)

    def __str__(self):
        result = []
        for item in self.items:
            result.append(str(item))
        return "\n".join(result)
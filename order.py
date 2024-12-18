from dessert import Dessert

class Order:
    def __init__(self):
        self.items = []

    def add(self, dessert_item):
        self.items.append(dessert_item)

    def order_cost(self):
        return sum(item.calculate_cost() for item in self.items)

    def order_tax(self):
        return sum(item.calculate_tax() for item in self.items)

    def get_data(self):
        data = [["Name", "Quantity", "Unit Price", "Cost", "Tax", "Packaging"]]

        for item in self.items:
            item_data = str(item).split("\n")
            item_data = [col.strip() for col in item_data]
            packaging = item.packaging
            data.append(item_data + [packaging])
        
        subtotal = self.order_cost()
        tax = self.order_tax()
        total = subtotal + tax
        data.append(["Order Subtotal", "", "", f"${subtotal:.2f}", f"${tax:.2f}", ""])
        data.append(["Order Total", "", "", f"${total:.2f}", "", ""])
        data.append(["Total items in the order", "", "", len(self.items), "", ""])

        return data

    def __str__(self):
        result = ["Order Summary:"]
        for item in self.items:
            result.append(f" - {item}")
        subtotal = self.order_cost()
        tax = self.order_tax()
        total = subtotal + tax
        result.append(f"\nSubtotal: ${subtotal:.2f}")
        result.append(f"Tax: ${tax:.2f}")
        result.append(f"Total: ${total:.2f}")
        return "\n".join(result)
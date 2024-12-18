from dessert import Candy, Cookie, IceCream, Sundae
import receipt

class DessertShop:
    @staticmethod
    def user_prompt_candy():
        name = input("Enter the type of candy: ")
        while True:
            try:
                weight = float(input("Enter the weight (lbs): "))
                if weight < 0:
                    raise ValueError("Weight must be a positive number.")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                price_per_pound = float(input("Enter the price per pound: "))
                if price_per_pound < 0:
                    raise ValueError("Price per pound must be a positive number.")
                break
            except ValueError as e:
                print(e)
        return Candy(name, weight, price_per_pound)

    @staticmethod
    def user_prompt_cookie():
        name = input("Enter the type of cookie: ")
        while True:
            try:
                quantity = int(input("Enter the quantity purchased: "))
                if quantity < 0:
                    raise ValueError("Quantity must be a positive number.")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                price_per_dozen = float(input("Enter the price per dozen: "))
                if price_per_dozen < 0:
                    raise ValueError("Price per dozen must be a positive number.")
                break
            except ValueError as e:
                print(e)
        return Cookie(name, quantity, price_per_dozen)

    @staticmethod
    def user_prompt_icecream():
        name = input("Enter the type of ice cream: ")
        while True:
            try:
                scoops = int(input("Enter the number of scoops: "))
                if scoops < 0:
                    raise ValueError("Number of scoops must be a positive number.")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                price_per_scoop = float(input("Enter the price per scoop: "))
                if price_per_scoop < 0:
                    raise ValueError("Price per scoop must be a positive number.")
                break
            except ValueError as e:
                print(e)
        return IceCream(name, scoops, price_per_scoop)

    @staticmethod
    def user_prompt_sundae():
        name = input("Enter the type of ice cream: ")
        while True:
            try:
                scoops = int(input("Enter the number of scoops: "))
                if scoops < 0:
                    raise ValueError("Number of scoops must be a positive number.")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                price_per_scoop = float(input("Enter the price per scoop: "))
                if price_per_scoop < 0:
                    raise ValueError("Price per scoop must be a positive number.")
                break
            except ValueError as e:
                print(e)
        topping = input("Enter the topping: ")
        while True:
            try:
                price_for_topping = float(input("Enter the price for the topping: "))
                if price_for_topping < 0:
                    raise ValueError("Price for the topping must be a positive number.")
                break
            except ValueError as e:
                print(e)
        return Sundae(name, scoops, price_per_scoop, topping, price_for_topping)

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
        data = [["Name", "Quantity", "Unit Price", "Cost", "Tax"]]

        for item in self.items:
            item_data = str(item).split(", ")
            data.append([col.strip() for col in item_data])
        

        subtotal = self.order_cost()
        tax = self.order_tax()
        total = subtotal + tax
        data.append(["Order Subtotal", "", "", f"${subtotal:.2f}", f"${tax:.2f}"])
        data.append(["Order Total", "", "", f"${total:.2f}", ""])
        data.append(["Total items in the order", "", "", len(self.items), ""])

        return data

def main():
    print("Welcome to the Dessert Shop!")
    order = Order()

    while True:
        print("\n1: Candy")
        print("2: Cookie")
        print("3: Ice Cream")
        print("4: Sundae")
        choice = input("What would you like to add to the order? (1-4, Enter for done): ").strip()
        if not choice:
            break
        elif choice == "1":
            order.add(DessertShop.user_prompt_candy())
        elif choice == "2":
            order.add(DessertShop.user_prompt_cookie())
        elif choice == "3":
            order.add(DessertShop.user_prompt_icecream())
        elif choice == "4":
            order.add(DessertShop.user_prompt_sundae())
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    print("\nReceipt:")
    print(order)

    data = order.get_data()
    pdf_path = "receipt.pdf"
    receipt.make_receipt(data, pdf_path)
    print(f"\nReceipt PDF has been saved to: {pdf_path}")

main()
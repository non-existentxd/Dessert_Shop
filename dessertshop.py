from dessert import Order, Candy, Cookie, IceCream, Sundae
from receipt import generate_receipt


class DessertShop:
    def user_prompt_candy(self):
        name = input("Enter the type of candy: ").strip()
        while True:
            try:
                weight = float(input("Enter the weight (in lbs): "))
                if weight < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid weight. Please enter a positive number.")

        while True:
            try:
                price_per_lb = float(input("Enter the price per pound: "))
                if price_per_lb < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid price. Please enter a positive number.")

        return Candy(name, weight, price_per_lb)

    def user_prompt_cookie(self):
        name = input("Enter the type of cookie: ").strip()
        while True:
            try:
                quantity = int(input("Enter the quantity purchased: "))
                if quantity < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid quantity. Please enter a positive integer.")

        while True:
            try:
                price_per_dozen = float(input("Enter the price per dozen: "))
                if price_per_dozen < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid price. Please enter a positive number.")

        return Cookie(name, quantity, price_per_dozen)

    def user_prompt_icecream(self):
        name = input("Enter the type of ice cream: ").strip()
        while True:
            try:
                scoops = int(input("Enter the number of scoops: "))
                if scoops < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid number of scoops. Please enter a positive integer.")

        while True:
            try:
                price_per_scoop = float(input("Enter the price per scoop: "))
                if price_per_scoop < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid price. Please enter a positive number.")

        return IceCream(name, scoops, price_per_scoop)

    def user_prompt_sundae(self):
        name = input("Enter the type of ice cream: ").strip()
        while True:
            try:
                scoops = int(input("Enter the number of scoops: "))
                if scoops < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid number of scoops. Please enter a positive integer.")

        while True:
            try:
                price_per_scoop = float(input("Enter the price per scoop: "))
                if price_per_scoop < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid price. Please enter a positive number.")

        topping = input("Enter the topping: ").strip()
        while True:
            try:
                topping_price = float(input("Enter the price for the topping: "))
                if topping_price < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid price. Please enter a positive number.")

        return Sundae(name, scoops, price_per_scoop, topping, topping_price)


def main():
    shop = DessertShop()
    order = Order()
    '''
    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    '''
    done: bool = False

    prompt = '\n'.join([ '\n',
            '1: Candy',
            '2: Cookie',
            '3: Ice Cream',
            '4: Sunday',
            '\nWhat would you like to add to the order? (1-4, Enter for done): '])
    while not done:
        choice = input(prompt)
        match choice:
            case '':
                done = True
            case '1':
                item = shop.user_prompt_candy()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '2':
                item = shop.user_prompt_cookie()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '3':
                item = shop.user_prompt_icecream()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case '4':
                item = shop.user_prompt_sundae()
                order.add(item)
                print(f'{item.name} has been added to your order.')
            case _:
                print('Invalid response: Please enter a choice from the menu (1-4) or Enter')
    print()




    order_items = []
    for item in Order.items:
        order_items.append({
                "  Name": item.name,
                "Item Cost": item.calculate_cost(),
                "Tax": item.calculate_tax()
            })

        subtotal = order.calculate_subtotal()
        tax = order.calculate_total_tax()
        total = order.calculate_total_cost()
        total_items = len(order.items)
        generate_receipt(order_items, subtotal, tax, total, total_items)
        print("Receipt saved as 'receipt.pdf'.")
    else:
        print("No items in the order. No receipt generated.")




if __name__ == "__main__":
    main()
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
cashier = MoneyMachine()
menu = Menu()
status = True

while(status):
    options = menu.get_items()
    order = input(f"What would like? ({options}): ")
    if order.lower() == "off":
        status = False
    elif order.lower() == "report":
        print(coffee_machine.report())
        print(cashier.report())
    else:
        drink = Menu.find_drink(menu, order.lower())
        if coffee_machine.is_resource_sufficient(drink) and cashier.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
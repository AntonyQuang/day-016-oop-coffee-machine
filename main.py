from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = Menu()
menu = coffee.get_items()
coffee_machine = CoffeeMaker()
money = MoneyMachine()

is_on = True
while is_on:
    choice = input(f"What would you like? ({menu}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        money.report()
    else:
        drink = coffee.find_drink(choice)

        if coffee_machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)




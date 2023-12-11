from Menu import MENU, resources
is_on = True
profit = 0


def make_coffee(drink_name, order_ingredients):
    """""Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


def is_resource_sufficient(order_ingredients):
    """"Checks if there are enough ingredients in the machine to make the order"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    """"Returns True if payment is accepted and False if payment is insufficient"""
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change: {change}$")
        return True
    else:
        print("Sorry that is not enough money. Money refunded")
        return False


def process_coins():
    """Return True when an order can be made and False when there is not enough money paid"""
    print("Please insert coins ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


while is_on:
    choice = input("What would you like? Espresso / Latte / Cappuccino : ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"the profit is {profit}$")
        print(f"Water {resources['water']}ml")
        print(f"Milk {resources['milk']}ml")
        print(f"Coffee {resources['coffee']}g")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "penny": 0.01
}

status = True
profit = 0

def actions(request):
    if (request.lower() == "report"):
        for key, value in resources.items():
            print(key,":", value)
    elif (request.lower() in ["espresso", "latte", "cappuccino"]):
        resource_check = check_resources(request.lower())
        if resource_check != "good":
            print("Sorry there is not enough " + resource_check)
        else:
            print("Please insert $" + str(MENU[request.lower()]["cost"]))
            payment = process_coins()
            if transaction(payment, MENU[request.lower()]["cost"]):
                make_coffee(request.lower())

def check_resources(menu_item):
    for key in MENU[menu_item]["ingredients"]:
        if MENU[menu_item]["ingredients"][key] > resources[key]:
            return key
    return "good"

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * coins["quarter"]
    total += int(input("How many dimes?: ")) * coins["dime"]
    total += int(input("How many nickles?: ")) * coins["nickle"]
    total += int(input("How many pennies?: ")) * coins["penny"]
    return total

def transaction(payment, price):
    global profit
    if payment > price:
        change = round(payment - price, 2)
        print(f"Thank you for your purchase and here is ${change} in change.")
        profit += payment
        return True
    elif payment == price:
        print("Thank you for your purchase!")
        profit += payment
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink):
    for key in MENU[drink]["ingredients"]:
        resources[key] -= MENU[drink]["ingredients"][key]
    print(f"Here is your {drink}. Enjoy!")

is_on = True

while(is_on):
    request = input("What would you like? (espresso/latte/cappaccino):")
    if (request.lower() == "off"):
        is_on = False
    else:
        actions(request)

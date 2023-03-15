MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
QUARTER = 0.25
DIME = 0.10
NICKELS = 0.05
PENNIES = 0.01


def get_milk():
    taken_milk = resources.get("milk")
    return taken_milk


def get_coffee():
    taken_coffee = resources.get("coffee")
    return taken_coffee


def get_water():
    taken_water = resources.get("water")
    return taken_water


def print_report():
    print(f"Water: {get_water()}ml")
    print(f"Milk: {get_milk()}ml")
    print(f"Coffee: {get_coffee()}g")
    print(f"Money: ${money}")


def check_if_resources_present(user_coffee):
    menu_water = MENU[user_coffee]["ingredients"]["water"]
    if get_water()-menu_water < 0:
        return False
    menu_coffee = MENU[user_coffee]["ingredients"]["coffee"]
    if get_coffee()-menu_coffee < 0:
        return False
    if "milk" in MENU[user_coffee]["ingredients"]:
        menu_milk = MENU[user_coffee]["ingredients"]["milk"]
        if get_milk()-menu_milk < 0:
            return False
    return True


def prepare_coffee(given_choice):
    menu_water = MENU[given_choice]["ingredients"]["water"]
    changed_water = get_water()-menu_water
    resources.update({"water": changed_water})

    menu_coffee = MENU[given_choice]["ingredients"]["coffee"]
    changed_coffee = get_coffee()-menu_coffee
    resources.update({"coffee": changed_coffee})

    if "milk" in MENU[given_choice]["ingredients"]:
        menu_milk = MENU[given_choice]["ingredients"]["milk"]
        changed_milk = get_milk()-menu_milk
        resources.update({"milk": changed_milk})

    menu_money = MENU[given_choice]["cost"]
    global money
    money += menu_money


def calculate_money(in_quarter, in_dime, in_nickel, in_pennies):
    return round(in_quarter*QUARTER + in_dime*DIME + in_nickel*NICKELS + in_pennies*PENNIES, 2)


def has_enough_money(given_choice, user_money):
    menu_money = MENU[given_choice]["cost"]
    return user_money-menu_money


should_continue = True
should_process_further = True

while should_continue:

    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
if user_choice in ("espresso", "latte", "cappuccino"):
        has_enough_resources = check_if_resources_present(user_choice)
        # print(has_enough_resources)
        if has_enough_resources:
            should_continue = True
            should_process_further= True
        else:
            should_continue = True
            should_process_further = False
            print("Sorry.. Resources not available at the moment")
    elif user_choice == "report":
        print_report()
        should_process_further = False
        should_continue = True
    elif user_choice == "off":
        should_continue = False
        should_process_further = False
    else:
        print("Invalid input")
        should_process_further = False
        should_continue = False

    if should_continue and should_process_further:
        print("Please insert coins : ")
        user_quarter = float(input("how many quarters?: "))
        user_dime = float(input("how many dimes?: "))
        user_nickels = float(input("how many nickels?: "))
        user_pennies = float(input("how many pennies?: "))
        user_input_money = calculate_money(user_quarter, user_dime, user_nickels, user_pennies)
        print(f"Total money : ${user_input_money}")

        checked_money = has_enough_money(user_choice, user_input_money)
        if checked_money >= 0:
            rounded_checked_money = round(checked_money, 2)
            print(f"Here is your change : ${rounded_checked_money}")
        else:
            print("Sorry that's not enough money. Money refunded.")
            should_continue = True
            should_process_further = False

        if should_continue and should_process_further:
            prepare_coffee(user_choice)
            print(f"Enjoy your {user_choice} ☕")

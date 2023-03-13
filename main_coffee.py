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


def print_report():
    water = resources.get("water")
    milk = resources.get("milk")
    coffee = resources.get("coffee")
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def calculate_money(in_quarter, in_dime, in_nickel, in_pennies):
    return in_quarter


# TODO 1 : Enter the option by user
user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
# TODO 2 : Repeat the prompt for user for next customer
# TODO 3 : Turn off the coffee machine by entering off
# TODO 4 : print report
if user_choice == "espresso":
    water = resources.get("water")
    milk = resources.get("milk")
    coffee = resources.get("coffee")
    resources.update({"water": (water-50), "milk": (milk-0), "coffee": (coffee-8)})
    print(resources)
elif user_choice == "report":
    print_report()
# TODO 5 : After user selects a drink, program should check if enough resources are present
# TODO 6 : Calculate the entered coins
print("Please insert coins : ")
user_quarter = input("how many quarters?: ")
user_dime = input("how many dimes?: ")
user_nickels = input("how many nickels?: ")
user_pennies = input("how many pennies?: ")
user_input_money = calculate_money(user_quarter, user_dime, user_nickels, user_pennies)
# TODO 7 : Check if transaction successful - if more offer change, if less reject transation
# TODO 8 : Make coffee if all okay and print a success message

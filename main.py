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


def check_if_there_is_enough_resources(answer):
    needed_resources = MENU[answer]["ingredients"]
    if answer == "espresso":
        if needed_resources["water"] <= resources["water"] and needed_resources["coffee"] <= resources["coffee"]:
            resources["water"] -= needed_resources["water"]
            resources["coffee"] -= needed_resources["coffee"]
            return True
        else:
            print("Not enough resources")
            return False
    else:
        if needed_resources["water"] <= resources["water"] and needed_resources["milk"] <= resources["milk"] and \
                needed_resources["coffee"] <= resources["coffee"]:
            resources["water"] -= needed_resources["water"]
            resources["milk"] -= needed_resources["milk"]
            resources["coffee"] -= needed_resources["coffee"]
            return True
        else:
            print("Not enough resources")
            return False


def return_user_answer():
    print("Welcome to CoffeMachine!")
    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if answer == "espresso" or answer == "latte" or answer == "cappuccino" or answer == "off" or answer == "report":
        return answer
    else:
        print("Sorry, that's not an option")
        return return_user_answer()


def main(coins, answer):
    if answer == "espresso" or answer == "latte" or answer == "cappuccino":
        print(f"You have chosen {answer}, your coins are: ${coins}")
        if check_if_there_is_enough_resources(answer):
            check_if_coins_are_enough(coins, answer)
            print(f"Here is your {answer}☕. Enjoy!")
    elif answer == "off":
        print("Coffe machine is turning down...")
        exit()
    elif answer == "report":
        print("Report is...")
        print(resources)


def calculate_user_coins(answer):
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    if answer == "espresso" or answer == "latte" or answer == "cappuccino":
        price = MENU[answer]["cost"]
        print(f"{answer} costs ${price}")
        quarters = int(input("How many quarters?"))
        dimes = int(input("How many dimes?"))
        nickles = int(input("How many nickles?"))
        pennies = int(input("How many pennies?"))
        sum_of_coins = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        return sum_of_coins
    else:
        return


def check_if_coins_are_enough(coins, answer):
    if answer == "espresso" or answer == "latte" or answer == "cappuccino":
        price = MENU[answer]["cost"]
        global resources
        global INCOME
        if coins >= price:
            rest = round(coins - price, 2)
            INCOME += price
            resources["income"] = INCOME
            print(f"Your rest is equal to {rest}")
            return True
        else:
            print("Sorry, that's not enough money! Money refunded")
            return False
    else:
        return False


loop = True
INCOME = 0
while loop:
    ANSWER = return_user_answer()
    COINS = calculate_user_coins(ANSWER)
    main(COINS, ANSWER)

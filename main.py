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
    "money": 0.00
}



def printReport():
    print(f"Water {resources['water']}")
    print(f"Milk {resources['milk']}")
    print(f"Coffee {resources['coffee']}")
    print(f"Money ${resources['money']}")

def checkResources(water,milk,coffee):
    availableWater = resources['water']
    availableMilk = resources['milk']
    availableCoffee = resources['coffee']

    if availableWater >= water and availableCoffee >= coffee and availableMilk >= milk:
        return True
    else:
        return False

def checkUserInput(userInput):
    if userInput == "off":
        return False
    elif userInput == "report":
        return "report"
    elif userInput == "espresso":
        return checkResources(50, 0, 18)
    elif userInput == "latte":
        return checkResources(200, 150, 24)
    elif userInput == "cappuccino":
        return checkResources(250, 100, 24)
    elif userInput == "add resources":
        return "add resources"
    else:
        print("Please enter Espresso, Latte, or Cappuccino")

def checkCoins(quarters, dimes, nickles, pennies, drink):
    totalQuarters = quarters * .25
    totalDimes = dimes * .10
    totalNickles = nickles * .05
    totalPennies = pennies * .01

    global userInput

    totalCoins = totalQuarters + totalDimes + totalNickles + totalPennies

    drinkCost = 0

    if drink == "espresso":
        drinkCost = MENU['espresso']['cost']
    elif drink == "latte":
        drinkCost = MENU['latte']['cost']
    elif drink == "cappuccino":
        drinkCost = MENU['cappuccino']['cost']

    if(totalCoins >= drinkCost):
        change = totalCoins - drinkCost
        change = round(change, 2)
        resources['water'] = resources['water'] - MENU['latte']['ingredients']['water']
        resources['milk'] = resources['milk'] - MENU['latte']['ingredients']['milk']
        resources['coffee'] = resources['coffee'] - MENU['latte']['ingredients']['coffee']
        print(f"Here is your change ${change}")
        print(f"Here is your {drink}")
        resources['money'] = resources['money'] + drinkCost
    else:
        print("Sorry that's not enough money. Money refunded.")

def addResources():
    water = int(input("How much water do you want to add? "))
    milk = int(input("How much water do you want to add? "))
    coffee = int(input("How much water do you want to add? "))

    resources['water'] = resources['water'] + water
    resources['milk'] = resources['milk'] + milk
    resources['coffee'] = resources['coffee'] + coffee

# TODO: 1. Print report of all coffee machine resources

def TurnOn():

    Machine_is_on = True

    while Machine_is_on:

        userInput = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO: 2. Check resources sufficient to make drink order
        check = checkUserInput(userInput)

        if check == False and userInput == "off":
            break
# TODO: 3. Process coins
        elif check != "report" and check != "add resources" and check != False:
           quarters = float(input("How many quarters? "))
           dimes = float(input("How many dimes? "))
           nickles = float(input("How many nickles? "))
           pennies = float(input("How many pennies? "))
# TODO: 4: Check transaction successful
# TODO: 5: Make Coffee
           checkCoins(quarters, dimes, nickles, pennies, userInput)
        elif check == "report":
            printReport()
        elif check == "add resources":
            addResources()
        else:
            print("Not enough resources")

TurnOn()
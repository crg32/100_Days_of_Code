import time

from menu import MENU
from decimal import Decimal, getcontext

getcontext().rounding = 'ROUND_HALF_EVEN'

Resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def runit():
    power = True
    while power:
        drinkchoice = prompt()
        if drinkchoice.lower() == "off":
            power = False
            print("Powering Down")
            return
        suitableResources = ingAmount(drinkchoice)
        if suitableResources:
            pay(drinkchoice)
            updateResources(drinkchoice)
    return


def prompt():
    print("What would you like? (espresso/latte/cappuccino):")
    order = input().lower()
    while order not in ["espresso", "cappuccino", "latte", "off"]:
        print(order, "is not available. Please go home or tell us what you want for real")
        print("What would you like? (espresso/latte/cappuccino):")
        order = input().lower()
    return order


def ingAmount(drink):
    if drink == "espresso":
        print("You chose espresso. We are confirming there are enough espresso ingredients")
        reqWater = MENU.get("espresso").get("ingredients").get("water")
        reqCoffee = MENU.get("espresso").get("ingredients").get("coffee")
        reqMilk = 0
    elif drink == "latte":
        print("You chose latte. We are confirming there are enough latte ingredients")
        reqWater = MENU.get("latte").get("ingredients").get("water")
        reqCoffee = MENU.get("latte").get("ingredients").get("coffee")
        reqMilk = MENU.get("latte").get("ingredients").get("milk")
    elif drink == "cappuccino":
        print("You chose cappuccino. We are confirming there are enough cappuccino ingredients")
        reqWater = MENU.get("cappuccino").get("ingredients").get("water")
        reqCoffee = MENU.get("cappuccino").get("ingredients").get("coffee")
        reqMilk = MENU.get("cappuccino").get("ingredients").get("milk")
    else:
        print("this is not one of the available beverages.")
        return False
    for x in range(3):
        print(".")
        time.sleep(1)
    toMakeOrNotToMake = isthereenough(reqWater, reqCoffee, reqMilk)
    return toMakeOrNotToMake


def isthereenough(wat, coff, milk):
    if Resources.get("water") < wat or Resources.get("coffee") < coff or Resources.get("milk") < milk:
        print("You do not have sufficient resources.")
        return False
    else:
        print("There are sufficient resources to make your drink")
        return True


def pay(drink):
    print("Your", drink, "costs $" + str(MENU[drink]["cost"]) + ". While your drink is being prepared, please insert coins to pay.")
    # Ask for the # of each coin
    # Then determine monetary value based on quantity
    quqty = int(input("How many quarters?: "))
    quvalue = quqty * 25

    diqty = int(input("How many dimes?: "))
    divalue = int(diqty) * 10

    niqty = int(input("How many nickels?: "))
    nivalue = int(niqty) * 5

    peqty = int(input("How many pennies?: "))
    pevalue = int(peqty) * 1

    cash = quvalue + divalue + nivalue + pevalue
    cash = cash / Decimal(100)
    change = cash - Decimal(MENU[drink]["cost"])
    print("You gave $" + str(cash) + " for your", drink +". Here is your change, $" + str(change) + ". Thank you!")
    return


def updateResources(drinkchoice):
    if "milk" in MENU[drinkchoice]["ingredients"]:
        Resources["milk"] -= MENU[drinkchoice]["ingredients"]["milk"]
    Resources["water"] -= MENU[drinkchoice]["ingredients"]["water"]
    Resources["coffee"] -= MENU[drinkchoice]["ingredients"]["coffee"]
    return


# print(Decimal(MENU["latte"]["cost"]))
runit()

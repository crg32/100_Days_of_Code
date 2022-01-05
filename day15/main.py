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
        print("drinkChoice is", drinkchoice)
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
        print("Checking espresso ingredients")
        reqWater = MENU.get("espresso").get("ingredients").get("water")
        reqCoffee = MENU.get("espresso").get("ingredients").get("coffee")
        reqMilk = 0
    elif drink == "latte":
        print("Checking latte ingredients")
        reqWater = MENU.get("latte").get("ingredients").get("water")
        reqCoffee = MENU.get("latte").get("ingredients").get("coffee")
        reqMilk = MENU.get("latte").get("ingredients").get("milk")
    elif drink == "cappuccino":
        print("Checking cappuccino ingredients")
        reqWater = MENU.get("cappuccino").get("ingredients").get("water")
        reqCoffee = MENU.get("cappuccino").get("ingredients").get("coffee")
        reqMilk = MENU.get("cappuccino").get("ingredients").get("milk")
    else:
        print("this is not one of the available beverages.")
        return False
    toMakeOrNotToMake = isthereenough(reqWater, reqCoffee, reqMilk)
    return toMakeOrNotToMake


def isthereenough(wat, coff, milk):
    water = Resources.get("water") - wat
    coffee = Resources.get("coffee") - coff
    milk = Resources.get("milk") - milk

    if wat < Resources.get("water") or coff < Resources.get("coffee") or milk < Resources.get("milk"):
        print("You do not have sufficient resources.")
        return False
    else:
        return True


def pay(drink):
    print("Please insert coins.")
    # Ask for the # of each coin
    # Then determine monetary value based on quantity
    quqty = int(input("How many quarters?: "))
    quvalue = quqty * 25

    diqty = int(input("How many dimes?: "))
    divalue = int(diqty) * 10

    niqty = int(input("How many nickes?: "))
    nivalue = int(niqty) * 5

    peqty = int(input("How many pennies?: "))
    pevalue = int(peqty) * 1

    cash = quvalue + divalue + nivalue + pevalue
    cash = cash / Decimal(100)
    change = cash - Decimal(MENU[drink]["cost"])
    print("You paid $", cash, " for ", drink, ". Here is your change, $", change, ". Thank you!")
    return


def updateResources(usedWater, usedMilk, usedCoffee):
    Resources["water"] -= usedWater
    Resources["milk"] -= usedMilk
    Resources["coffee"] -= usedCoffee
    return


# print(Decimal(MENU["latte"]["cost"]))
ingAmount("espresso")
# runit()

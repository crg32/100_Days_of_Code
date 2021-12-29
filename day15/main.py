from menu import MENU
from decimal import Decimal, getcontext

getcontext().rounding = 'ROUND_HALF_EVEN'


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def runit():
    power = True
    while power:
        drinkchoice = prompt()
        print("drinkChoice is",  drinkchoice)
        if drinkchoice.lower() == "off":
            power = False
            print("Powering Down")
            return
        suitableResources = checkIngredients(drinkchoice)
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

def checkIngredients(drink):
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

    water = resources.get("water") - reqWater
    coffee = resources.get("coffee") - reqCoffee
    milk = resources.get("coffee") - reqMilk

    if water < 0 or coffee < 0 or milk < 0:
        print("You do not have sufficient resources.")
        return False
    else:
        print("All ingredients found. Making beverage")
        updateResources(water, milk, coffee)
        return True


def pay(drink):
    print("Please insert coins.")
    #Ask for the # of each coin
    #Then determine monetary value based on quantity
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

def updateResources(water, milk, coffee):
    MENU.update({water: water})
    print(MENU[water])
#    car.update({"color": "White"})


#print(Decimal(MENU["latte"]["cost"]))
updateResources(20,0,0)
#runit()

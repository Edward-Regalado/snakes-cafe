from textwrap import dedent

# welcome text

def welcome():
    print("**************************************")
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("** ")
    print("** To quit at any time, type \"quit\" **")
    print("**************************************")

# Order text

def order():
    print("***********************************")
    print("** What would you like to order? **")
    print("***********************************")

menu = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0, 
    "Unicorn Tears": 0,
}

menu = dedent
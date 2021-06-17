from textwrap import dedent

# this is the welcome text which greets the user 
def welcome():
   print('\n \n ************************************** \n **    Welcome to the Snakes Cafe!   ** \n **    Please see our menu below.    ** \n ** \n ** To quit at any time, type "quit" ** \n **************************************\n')

# this is the order prompt text for the user
def order():
    print(" *********************************** \n ** What would you like to order? ** \n *********************************** \n")

# menu items 
menu_list = {
    "Wings": 0, 
    "Cookies": 0,
    "Spring Rolls": 0, 
    "Salmon": 0, 
    "Steak": 0, 
    "Meat Tornado": 0, 
    "A Literal Garden": 0, 
    "Ice Cream": 0, 
    "Cake": 0, 
    "Pie": 0, 
    "Coffee": 0, 
    "Tea": 0, 
    "Unicorn Tears": 0,
}

# formatted menu items that get printed for user
menu_dict = dedent("""
Appetizers
----------
{}
{}
{}
Entrees
----------
{}
{}
{}
{}
Desserts
----------
{}
{}
{}
Drinks
----------
{}
{}
{}
""".format(*menu_list)
)

# prints welcome text
welcome()
# prints menu
print(menu_dict)
# prints what would you like to order?
order()

user_input = input('> ').lower()
user_input = user_input.capitalize()
# print(f"user_input is {user_input}")
added_items = {}

# logic for adding menu items
while user_input != "Quit":

    if user_input not in menu_list:
        print("**  Please order from the menu  **")
    
    if user_input in menu_list:
        if user_input not in added_items:
            added_items[user_input] = 0
        added_items[user_input] += 1
        print(f"** {added_items[user_input]} order of {user_input} have been added to your meal **")
    user_input = input('> ').lower()
    user_input = user_input.capitalize()

if user_input == "Quit":
    if added_items == {}:
        print("** Thank you, have a nice day **")
    else:
        print(f"** Your order: **")
        for each in added_items.keys():
            print(f"{each} {added_items[each]}")
        print("** Your order is coming right up! **")
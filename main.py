import datetime
from users import Users, login
from items import Item, displayItems
from pos import POS

# Define users
users = [Users("admin", "prologi"), Users("user2", "password2")]

pos = POS()
items = [
    Item("Claw Hammer", 280, 100),
    Item("Interchangeable Screwdriver Set", 400, 70),
    Item("Combination Wrench Set", 1200, 60),
    Item("Cordless Power Drill", 4000, 25),
    Item("Drill Bit Set", 600, 50),
    Item("Carbon steel nails", 50, 200),
    Item("Hand Saw", 450, 80),
    Item("Grit Sandpaper", 20, 800),
    Item("Hand Axe", 450, 100),
    Item("Ball Bearings Set", 700, 100),
    Item("Level Leveling Tool", 500, 40),
    Item("Tape Measure", 180, 150),
    Item("Bolt Cutters", 600, 60),
    Item("Duct Tape", 150, 300),
    Item("Hardware Assortment Kit", 700, 100),
    Item("Vise Grip", 400, 80),
    Item("WD-40 277mL", 300, 350),
    Item("Socket Wrench Set", 1200, 60),
    Item("Staple Gun", 650, 50),
    Item("Staples", 200, 200)
]

while True:
    if login(users):  # Login loop
        while True:  # Shopping loop
            displayItems(items)

            while True:
                choice = input("\nSelect an item number or enter 'x' to proceed to checkout: ")

                if choice.lower() == 'x':
                    break
                try:
                    item_number = int(choice)
                    selected_item = items[item_number - 1]
                    quantity = int(input("Enter quantity: "))
                    pos.updateCart(selected_item, quantity)
                except (ValueError, IndexError):
                    print("Invalid choice. Please try again.")

            pos.checkout()

            while True:
                new_purchase = input("Enter 'z' to make another purchase or 'x' to exit the program: ")
                if new_purchase.lower() == 'x':
                    break
                elif new_purchase.lower() == 'z':
                    break
                else:
                    print("Invalid option. Please try again.")

            if new_purchase.lower() == 'x':
                break  # Exit the shopping loop and return to the login loop

class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

def displayItems(items):
    print("\nAvailable Items:")
    print("{:<5} {:<35} {:<10} {:<20}".format("No.", "Item", "Price", "Stock"))
    print("-" * 65)
    for i, item in enumerate(items, start=1):
        print("{:<5} {:<35} ₱{:<10} {:<20}".format(i, item.name, item.price, item.stock))

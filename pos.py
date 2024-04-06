import datetime

class POS:
    def __init__(self):
        self.cart = []
        self.total = 0

    def updateCart(self, item, quantity):
        if item.stock >= quantity:
            self.cart.append((item, quantity))
            self.total += item.price * quantity
            print(f"{quantity} {item.name}(s) added to cart.")
        else:
            print(f"Sorry, only {item.stock} {item.name}(s) available.")

    def displayCart(self, discount=0):
        print("Your Cart:")
        for item, quantity in self.cart:
            print(f"{item.name} x{quantity}")
        discounted_total = self.total * (1 - discount)
        print(f"Total (before discount): ₱{discounted_total:.2f}")

    def processReceipt(self, payment):
        discount = 0
        discount_option = input("\nSelect discount option: 1 - None, 2 - Senior, 3 - PWD, 4 - Others: ")
        if discount_option == '2':
            discount = 0.10  # 10% discount for seniors
        elif discount_option == '3':
            discount = 0.20  # 20% discount for PWDs
        elif discount_option == '4':
            discount = 0.15  # 15% discount for others

        discounted_total = self.total * (1 - discount)
        change = payment - discounted_total
        if change >= 0:
            receipt = "\nReceipt:\n"
            receipt += "{:<15} {:<10} {:<10} {:<10}\n".format("Item", "Price", "Quantity", "Total")
            receipt += "-" * 45 + "\n"
            for item, quantity in self.cart:
                total_price = item.price * quantity
                receipt += "{:<15} ₱{:<10.2f} {:<10} ₱{:<10.2f}\n".format(item.name, item.price, quantity, total_price)
            receipt += "-" * 45 + "\n"
            receipt += "Total (after discount): ₱{:.2f}\n".format(discounted_total)
            receipt += "Discount: {:.0%}\n".format(discount)
            receipt += "Payment: ₱{:.2f}\n".format(payment)
            receipt += "Change: ₱{:.2f}\n".format(change)

            now = datetime.datetime.now()
            receipt += f"Date: {now.strftime('%Y-%m-%d')}\n"
            receipt += f"Time: {now.strftime('%H:%M:%S')}\n"

            print(receipt)
        else:
            print("Insufficient payment. Please try again.")

    def checkout(self):
        self.displayCart()

        while True:
            action = input("\nEnter the payment amount or 'z' to cancel and empty cart: ")
            if action.lower() == 'z':
                print("\nTransaction cancelled.")
                self.cart = []  # Clear the cart
                self.total = 0  # Reset the total
                return

            try:
                payment = float(action)
                if payment < self.total:
                    print("Payment should be greater than or equal to the total cost.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

        self.processReceipt(payment)

        for item, quantity in self.cart:
            item.stock -= quantity
        self.cart = []
        self.total = 0
        print("\nTransaction completed. Thank you for your purchase!")

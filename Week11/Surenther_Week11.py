# DSC 510
# Week 11
# Programming Assignment Week 11 [ Object Oriented Programming ]
# Author Surenther Selvaraj

# Change History
# 05/22/2024  Week11 Assignment Initial Development         - Surenther Selvaraj

import locale


class CashRegister:
    num_of_item = 0  #Class variable for counting no of items
    total_price = 0  #Class variable for calculating total price of all items

    def additem(self, price):  #Method for adding items
        CashRegister.num_of_item += 1
        CashRegister.total_price += price

    def gettotal(): #Method for retrieving total price
        return CashRegister.total_price

    def getcount(): #Method for retrieving count of items
        return CashRegister.num_of_item


def main():
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
    keep_going = True
    print("Welcome")
    while keep_going:
        price = input("Please Enter the price for the item. Press 'q' to quit:  ") #Get the price from the user
        if price.lower() == "q":
            if CashRegister.getcount() == 0: #Asking user to add items before quiting
                print("No items in the cart. Please add some items")
            else:
                print(
                    "\nTotal items in the cart: {} \nTotal price of the items: {}".format(
                        CashRegister.getcount(),
                        locale.currency(CashRegister.gettotal(), grouping=True),
                    )
                )
                print("\nThanks for Shopping with us")
                keep_going = False
        else:
            try:
                price = float(price)
            except ValueError:
                print("Sorry, that is not a number . Try again.")
            else:
                if price > 0:
                    item = CashRegister()
                    item.additem(price)
                else:
                    print("The Price must be greater than 0")


if __name__ == "__main__":
    main()

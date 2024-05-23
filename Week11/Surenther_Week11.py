# DSC 510
# Week 11
# Programming Assignment Week 11 [ Object Oriented Programming ]
# Author Surenther Selvaraj

# Change History
# 05/22/2024  Week11 Assignment Initial Development         - Surenther Selvaraj

import locale

class cashregister:
    num_of_item = 0
    total_price = 0
    
    def additem(self,price):
        cashregister.num_of_item += 1
        cashregister.total_price += price
    
    def gettotal():
        return cashregister.total_price
    
    def getcount():
        return cashregister.num_of_item
    
def main():
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
    keep_going = True
    print ("Welcome")
    while keep_going:
        price = input("Please Enter the price for the item. Press 'q' to quit:  ")
        if price.lower() == "q":
            if (cashregister.getcount() == 0):
                print("No items in the cart. Please add some items")
            else:
                print("\nTotal items in the cart: {} \nTotal price of the items: {}".format(cashregister.getcount(),locale.currency(cashregister.gettotal(),grouping=True)))
                print("\nThanks for Shopping with us")
                keep_going = False 
        else:
            try:
                price = float(price)
            except ValueError:
                print("Sorry, that is not a number . Try again.")
            else:
                if price > 0:
                    item = cashregister()
                    item.additem(price)
                else:
                    print ("The Price must be greater than 0")

if __name__ == "__main__":
    main()
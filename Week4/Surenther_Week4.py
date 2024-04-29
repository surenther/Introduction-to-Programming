# DSC 510
# Week 4
# Programming Assignment Week 4 [Functions ]
# Author Surenther Selvaraj

# Change History
# 03/18/2024  Week2 Assignment Initial Development         - Surenther Selvaraj
# 03/25/2024  Week3 Assignment added Conditional Execution - Surenther Selvaraj
# 04/01/2024  Week4 Assignment added Functions             - Surenther Selvaraj

import locale


# Defining Calculation Function
def costcalculation(feet, price=0.87):
    return float(feet) * price


# Defining Receipt Function
def printreceipt(company, feet, cost, savings):
    print(
        "\n"
        + "Company Name: "
        + company
        + "\n"
        + "No of feet: "
        + "{:.2f}".format(feet)
        + "\n"
        + "Total Cost: "
        + cost
        + "\n"
        + "Total Savings: "
        + savings
    )


# Defining main Function
def main():
    # Setting Locale
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

    # Getting Username
    user_name = input("What is your name?\n")
    if user_name == "":
        print("Please enter name")
        exit()
    else:
        print("Hello " + user_name)

    # Getting Company Name
    company = input("Please enter Company Name\n")
    if company == "":
        print("Please enter Company name")
        exit()

    # Accept only no for the feet
    try:
        # Getting Feet
        feet = float(input("Please enter the no of feet of fiber optic cable\n"))
    except ValueError:
        print("Please enter a number")
    else:
        costwithout_discount = costcalculation(feet)
        # Calculating Installation Costs based on feet
        if feet > 500:
            cost = costcalculation(feet, 0.50)
        elif feet > 250:
            cost = costcalculation(feet, 0.70)
        elif feet > 100:
            cost = costcalculation(feet, 0.80)
        else:
            cost = costwithout_discount

        # Calculating Savings and print receipt
        savings = costwithout_discount - cost
        cost = locale.currency(cost, grouping=True)
        savings = locale.currency(savings, grouping=True)
        printreceipt(company, feet, cost, savings)


if __name__ == "__main__":
    main()

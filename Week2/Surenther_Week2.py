# DSC 510
# Week 2
# Programming Assignment Week 2 [ Variables and Math Operations ]
# Author Surenther Selvaraj

# Change History
# 03/18/2024  Initial Development Surenther Selvaraj

# Getting Username,Company and Feet details from the user
UserName = input("What is your name?\n")
print("Hello " + UserName)
Company = input("Please enter Company Name\n")
Feet = input("Please enter the no of feet of fiber optic cable\n")
# Accept only no for the feet
try:
    # Calculating Installation Costs
    Cost = float(Feet) * 0.87
    print("\n" + "Here is your Receipt")
    print(
        "Company Name: "
        + Company
        + "\n"
        + "No of feet: "
        + Feet
        + "\n"
        + "Total Cost: $"
        + str(round(Cost, 2))
    )
except ValueError:
    print("Please enter a number")

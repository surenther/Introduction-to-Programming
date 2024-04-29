# DSC 510
# Week 5
# Programming Assignment Week 4 [Loops ]
# Author Surenther Selvaraj

# Change History
# 04/08/2024  Week5 Assignment Initial Development         - Surenther Selvaraj


# Defining Calculation Function for performing mathematics operation
def perform_calculation(symbol):
    if symbol in ("+", "-", "*", "/"):
        try:
            num_1 = int(input("Enter First number: "))
            num_2 = int(input("Enter Second number: "))
        except ValueError:
            print("Please enter a number")
        else:
            if symbol == "+":
                return num_1 + num_2
            elif symbol == "-":
                return num_1 - num_2
            elif symbol == "*":
                return num_1 * num_2
            elif symbol == "/":
                return num_1 / num_2
    else:
        print("Please enter any of these char for specific operation +,-,*,/")


# Defining Calculation Function for performing Average
def calculate_average():
    total = 0
    count = 0
    try:
        iteration = int(input("Enter number you which to input: "))
    except ValueError:
        print("Please enter a number")
    else:
        for cntr in range(iteration):
            try:
                num = int(input("Enter " + str(cntr + 1) + " number: "))
            except ValueError:
                print("Please enter number")
                count = 0
                break
            else:
                total += num
                count += 1
        if count > 0:
            print(f"\nAverage is {round(total / count, 2)}\n")


# Defining main Function
def main():
    keep_going = True
    # while loop for executing the calculation till the user want to quit
    while keep_going:
        execution = input(
            "\nType 1 for Mathematics Calculation. Type 2 for Average Calculation. Type any other value to quit: "
        )
        # calling mathematics function
        if execution == "1":
            print("\nMathematics Calculation \n")
            symbol = input("Please Enter + or - or * or /: ")
            val = perform_calculation(symbol)
            if val is not None:
                print('Result:'+ str(round(val,2)))
        # calling average function
        elif execution == "2":
            print("\nAverage Calculation \n")
            calculate_average()
        else:
            print("\nGood Bye \n")
            keep_going = False


if __name__ == "__main__":
    main()

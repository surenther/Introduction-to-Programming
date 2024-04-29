# DSC 510
# Week 6
# Programming Assignment Week 6 [Strings & Loops]
# Author Surenther Selvaraj

# Change History
# 04/18/2024  Week6 Assignment Initial Development         - Surenther Selvaraj

# Defining function for calculating max, min & count of the list
def list_calculation(list_value):
    print('\n Maximum Temperature: ' + str(max(list_value)))
    print('\n Minimum Temperature: ' + str(min(list_value)))
    print('\n Total values of Temperature: ' + str(len(list_value)) + '\n')


# Defining main Function
def main():
    temperature = []
    keep_going = True
    # while loop for getting temperature
    while keep_going:
        temp_value = input("Enter temperature value or type 'q' to exit: ")
        if temp_value.lower() == 'q':
            list_calculation(temperature)
            keep_going = False
        else:
            try:
                temp_value = float(temp_value)
            except ValueError:
                print("Please enter a valid number")
            else:
                temperature.append(temp_value)


if __name__ == "__main__":
    main()

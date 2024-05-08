# DSC 510
# Week 9
# Programming Assignment Week 9 [ File Operations, Error Handling]
# Author Surenther Selvaraj

# Change History
# 04/27/2024  Week8 Assignment Initial Development         - Surenther Selvaraj
# 05/07/2024  Week9 Added File handling Process            - Surenther Selvaraj

import sys
import os

# Defining add_word function for adding word into dictionary
def add_word(word, dict):
    if word in dict:
        dict[word] += 1  # Increment the word count if the word already present
    else:
        dict[word] = 1  # Add the word count as 1 if the word is not already present


# Defining process_line function for processing each line
def process_line(line, dict):
    word_list = line.split()  # Get all the Words in the line
    for word in word_list:
        if word.isalnum() == True:  # Check if the word is Alpha Numeric
            word = word.lower()  # Convert all the word into lower case
        else:
            word = "".join(
                ch for ch in word if ch.isalnum()
            ).lower()  # Remove the special chars from the word and make it lower case
        add_word(word, dict)  # Add the word to dictonary


# Defining process file function for writing into a file
def process_file(dict, file_name):
    with open(file_name, "a") as filehandle:
        # Sort the dictnoary value based on the count
        dict_sorted = sorted(dict, key=dict.get, reverse=True)
        for word in dict_sorted:
            filehandle.write(
                "{:<20} {:<20} \n".format(word, dict[word])
            )  # write in decending order


# Defining main Function
def main():
    file_location = (os.path.dirname(__file__)) # Get current location
    try:
        file = open(os.path.join(file_location,'gettysburg.txt'),'r') # Read File
    except FileNotFoundError:
        print("File was not found")
    else:
        file_name = input("Enter the file name without any extenstion: ") # get filename from user
        if "." in file_name:
            print("Please enter the name with out .")
            sys.exit()
        else:
            file_name = file_name + ".txt"
            word_count = {}
            for line in file:
                process_line(line, word_count)
            del word_count[""]  # Remove the space from the Dictonary
        
            file_status = os.path.isfile(os.path.join(file_location,file_name))
            if file_status is False:          
                with open(file_name, "w") as filehandle: #Create file with user defined name
                    filehandle.write(
                        "\nThe Length of the dictonary: {}\n".format(len(word_count))
                    )
                    filehandle.write(
                        "\n{:<20} {:<20} \n{:<0}\n".format(
                            "Word", "Count", "---------------------------"
                            )
                    ) # Write total dictonary count to the file
                process_file(word_count, file_name)
                file.close()  # Close file
            else:
                print ('File Already present')
if __name__ == "__main__":
    main()

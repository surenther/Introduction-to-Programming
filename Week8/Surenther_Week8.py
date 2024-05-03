# DSC 510
# Week 8
# Programming Assignment Week 8 [ Dictionaries, Tuples, and JSON Data]
# Author Surenther Selvaraj

# Change History
# 04/27/2024  Week8 Assignment Initial Development         - Surenther Selvaraj


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


# Defining Preety_print function for printing
def preety_print(dict):
    print("\nThe Length of the dictonary: {}".format(len(dict)))
    print(
        "\n{:<20} {:<20} \n{:<0}".format("Word", "Count", "---------------------------")
    )
    dict_sorted = sorted(
        dict, key=dict.get, reverse=True
    )  # Sort the dictnoary value based on the count
    for word in dict_sorted:
        print("{:<20} {:<20}".format(word, dict[word]))  # print in decending order


# Defining main Function
def main():
    try:
        file = open("gettysburg.txt", "r")  # Read File
    except FileNotFoundError:
        print("File was not found")
    else:
        word_count = {}
        for line in file:
            process_line(line, word_count)
        del word_count[""]  # Remove the space from the Dictonary
        preety_print(word_count)
    file.close()  # Close file


if __name__ == "__main__":
    main()

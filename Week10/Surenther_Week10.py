# DSC 510
# Week 10
# Programming Assignment Week 10 [ Web Services ]
# Author Surenther Selvaraj

# Change History
# 05/14/2024  Week10 Assignment Initial Development         - Surenther Selvaraj

import requests
import json
import time

# Function for calling URL using requests
def req_url(url, param=""):
    try:
        if param == "":
            call_url = requests.get(url)
        else:
            call_url = requests.get(url, params=param)
    except requests.exceptions.ReadTimeout:
        raise SystemExit("Timeout.Not able to Reach URL")
    except requests.exceptions.ConnectionError:
        raise SystemExit("Connection Error. Not able to Reach URL")
    except requests.exceptions.RequestException:
        raise SystemExit("Unknown error occured")
    else:
        return call_url.text


# Function for calling list of category from chucknorris
def call_category():
    url = "https://api.chucknorris.io/jokes/categories"
    categories = json.loads(req_url(url))
    cntr = 1
    category_dict = {}
    for value in categories:
        category_dict[cntr] = value
        cntr = cntr + 1
    return category_dict


# Function for calling joke based on the category selected from chucknorris
def call_joke(param):
    url = "https://api.chucknorris.io/jokes/random"
    joke = json.loads(req_url(url, param))
    return joke


# Function for display
def preety_print(dict):
    print(
        "\n Category Selected: {} \n \n Joke: {} \n".format(
            "".join(dict["categories"]), dict["value"]
        )
    )


def main():
    category_dict = call_category()  # Dictonary with list of categories
    keep_going = True
    while keep_going:
        time.sleep(2)  # delay to show the joke
        category = input(
            "Category Selections:\n"
            + "\n".join(
                "Type '{}' for {}".format(key, value)
                for key, value in category_dict.items()
            )
            + "\n\nType 'X' to Exit"
            + "\n \n"
        )
        if category.lower() == "x":
            print("\n Good Bye \n")
            keep_going = False
        else:
            try:
                category = int(category)
            except ValueError:
                print("Sorry, that is not an integer . Try again.")
            else:
                category_value = category_dict.get(category)
                if category_value:
                    param = {"category": category_dict[category]}
                    preety_print(call_joke(param))
                else:
                    print("Please Select right Category")


if __name__ == "__main__":
    main()

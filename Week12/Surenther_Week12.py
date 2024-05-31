# DSC 510
# Week 11
# Programming Assignment Week 12 [ Final Project ]
# Author Surenther Selvaraj

# Change History
# 05/22/2024  Week12 Initial Development         - Surenther Selvaraj

import requests
import json
import sys
import re

app_id = "1b93174e0a0a4f0c8cc7032582e21b6b"


# Function for calling URL using requests
def req_url(url):
    try:
        call_url = requests.get(url)
    except requests.exceptions.ReadTimeout:
        raise SystemExit("Timeout.Not able to Reach URL")
    except requests.exceptions.ConnectionError:
        raise SystemExit("Connection Error. Not able to Reach URL")
    except requests.exceptions.RequestException:
        raise SystemExit("Unknown error occured")
    else:
        return call_url.text, call_url.status_code


# Function for Exception handling based on status
def requests_code(status):
    if status == 400:
        print("Error 400 - Bad Request")
    elif status == 401:
        print("Error 401 - Unauthorized")
    elif status == 404:
        print("Error 404 - No Data Found")
    elif status == 429:
        print("Error 429 - Quota exceeded")
    else:
        print("Unknown error occured")


# Function for input exception handling
def input_validation(value, sys_exit=""):
    # City name should be only chars
    if sys_exit == "city" and bool(re.search(r"\d", value)):
        print("Please enter only letters, not numbers.")
        return "error"
    # Zip code should be only 5 digit number
    elif sys_exit == "zip" and len(value) != 5:
        print("Please enter Five Digit Number.")
        return "error"
    elif value.lower() == "x":  # handling the program exist
        if sys_exit == "":
            print("\nThank you for using our application. Have a great day!\n")
            sys.exit()  # Stop Execution if the user type x
        # zip and temperature unit selection should not exit the program
        elif sys_exit == "temp" or sys_exit == "zip":
            print("Please enter a number instead of characters.")
            return "error"
        elif sys_exit == "city":  # city selection should not exit the program
            return value
        else:
            return "error"
    else:
        if sys_exit == "city":
            return value
        else:
            try:
                # Other the city search all the input should be only intgers.
                value_key = int(value)
            except ValueError:
                print("Please enter a number instead of characters.")
                return "error"
            else:
                return value_key


# Function for identifying Latitude and Longitude based on City Name
def city_search(city):
    url = (
        "http://api.openweathermap.org/geo/1.0/direct?q="
        + city
        + ",US"  # limiting search only to US
        + "&limit=5"
        + "&appid="
        + app_id
    )
    lat = json.loads(req_url(url)[0])
    status = req_url(url)[1]  # Get the status of the request
    city_merge = ""
    if status == 200:
        if (len(lat)) > 0:
            # Ask user to select the city based on the input value
            for key, value in enumerate(lat):
                if (
                    "state" not in value
                ):  # Some times API is not returing data for State. if no state then don't add state in the selection
                    city = "Type '{}' for {},{}".format(
                        key, value["name"], value["country"]
                    )
                else:
                    city = "Type '{}' for {},{},{}".format(
                        key, value["name"], value["state"], value["country"]
                    )
                city_merge = city_merge + "\n" + city
            city = input(
                "".join(
                    "\nPlease select your city: \n"
                    + city_merge
                    + "\nType 'X' to Exit"
                    + "\n \n"
                )
            )
            city_key = input_validation(city, "city_search")
            if city_key != "error":
                if city_key >= len(lat):
                    print("Please select the correct option.")
                else:
                    # Return Latitude and Longitude
                    return lat[city_key]["lat"], lat[city_key]["lon"]
        else:
            print("\nApologies, no data was found for the search term '" + city + "'")
    else:
        requests_code(status)
        sys.exit()  # Stop execution if there was an status error.


# Function for identifying Latitude and Longitude based on Zip
def zip_search(zip):
    zip = str(zip)
    url = (
        "http://api.openweathermap.org/geo/1.0/zip?zip="
        + zip
        + ","
        + "US"  # limiting search only to US
        + "&appid="
        + app_id
    )
    lat = json.loads(req_url(url)[0])
    status = req_url(url)[1]
    if status == 200:
        return lat["lat"], lat["lon"]  # Return Latitude and Longitude
    elif status == 404:  # 404 returned for no data
        print("\nApologies, no data was found for the search term '" + zip + "'")
        return "No Data"
    else:
        requests_code(status)
        sys.exit()  # Stop execution if there was an status error.


# Function for identifying Weather based on Latitude and Longitude
def weather(lat, long):
    # Ask user to select the Unit type
    unit = input(
        "\nPlease select your preferred temperature unit:\nType '1' for Fahrenheit\nType '2' for Celsius\nType any number for Kelvin\n\n"
    )
    unit_val = input_validation(unit, "temp")
    if unit_val != "error":
        match unit_val:
            case 1:
                unit = "imperial"
                symb = "\N{DEGREE SIGN}" + "F"  # Fahrenheit Symbol
            case 2:
                unit = "metric"
                symb = "\N{DEGREE SIGN}" + "C"  # Celsius Symbol
            case _:
                unit = "standard"
                symb = ""

        url = (
            "https://api.openweathermap.org/data/2.5/weather?lat="
            + str(lat)
            + "&lon="
            + str(long)
            + "&appid="
            + app_id
            + "&units="
            + unit
        )
        weather = json.loads(req_url(url)[0])
        status = req_url(url)[1]
        if status == 200:
            # Display weather information
            preety_print(weather, symb)
        else:
            requests_code(status)
            sys.exit()  # Stop execution if there was an status error.


# Function for displaying Weather information
def preety_print(climate, symb):
    print(
        "\nWeather Details\n----------------\nCity: {}\nCurrent Temp: {}{}\nFeels Like: {}{}\nMin Temp: {}{}\nMax Temp: {}{}\nHumidity: {}%\nPressure: {} hPa\nDescription: {}".format(
            climate["name"],
            climate["main"]["temp"],
            symb,
            climate["main"]["feels_like"],
            symb,
            climate["main"]["temp_min"],
            symb,
            climate["main"]["temp_max"],
            symb,
            climate["main"]["humidity"],
            climate["main"]["pressure"],
            climate["weather"][0]["description"].title(),
        )
    )


def main():
    keep_going = True
    print(
        "\nWelcome to the Weather app. This application allows you to retrieve weather details for any location within the USA."
    )
    while keep_going:
        # Ask User to select the Search type
        option = input(
            "\nPlease select an option:\n1 - Search by City name in the USA\n2 - Search by ZIP code in the USA\nX - Exit\n\n"
        )
        option_val = input_validation(option)
        if option_val != "error":
            if option_val == 1:
                city = input("Please enter the City name: ")
                city_val = input_validation(city, "city")
                if city_val != "error":
                    # Calling city search function by passing user typed city value
                    city_lat = city_search(city_val)
                    if city_lat is None:
                        print("")
                    else:
                        lat, long = city_lat
                        weather(lat, long)

            elif option_val == 2:
                zip = input("Please enter the ZIP code: ")
                zip_val = input_validation(zip, "zip")
                if zip_val != "error":
                    if zip_search(zip_val) == "No Data":
                        print(" ")
                    else:
                        # Calling zip search function by passing user typed zip value
                        lat, long = zip_search(zip)
                        weather(lat, long)

            else:
                print("Please select the correct option.")


if __name__ == "__main__":
    main()

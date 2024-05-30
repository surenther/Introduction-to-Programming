# DSC 510
# Week 11
# Programming Assignment Week 12 [ Final Project ]
# Author Surenther Selvaraj

# Change History
# 05/22/2024  Week12 Initial Development         - Surenther Selvaraj

import requests
import json
import sys

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
        print("Unexpected error")


# Function for input exception handling
def input_validation(value):
    if value.lower() == "x":
        print("\n Good Bye \n")
        sys.exit()  # Stop Execution if the user type x
    else:
        try:
            value_key = int(value)
        except ValueError:
            print("Sorry, that is not an integer . Try again.")
            return "error"
        else:
            return value_key


# Function for identifying Latitude and Longitude based on City Name
def city_search(city):
    url = (
        "http://api.openweathermap.org/geo/1.0/direct?q="
        + city
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
                if "state" not in value:
                    city = "Type '{}' for {} ,{}".format(
                        key, value["name"], value["country"]
                    )
                else:
                    city = "Type '{}' for {} in {},{}".format(
                        key, value["name"], value["state"], value["country"]
                    )
                city_merge = city_merge + "\n" + city
            city = input("".join(city_merge + "\n\nType 'X' to Exit" + "\n \n"))
            city_key = input_validation(city)
            if city_key != "error":
                if city_key >= len(lat):
                    print("Please Select right City")
                else:
                    # Return Latitude and Longitude
                    return lat[city_key]["lat"], lat[city_key]["lon"]
        else:
            print("\nNo Data Found ")
    else:
        requests_code(status)
        sys.exit()  # Stop execution if there was an status error.


# Function for identifying Latitude and Longitude based on Zip
def zip_search(zip, country):
    url = (
        "http://api.openweathermap.org/geo/1.0/zip?zip="
        + zip
        + ","
        + country
        + "&appid="
        + app_id
    )
    lat = json.loads(req_url(url)[0])
    status = req_url(url)[1]
    if status == 200:
        return lat["lat"], lat["lon"]  # Return Latitude and Longitude
    else:
        requests_code(status)
        sys.exit()  # Stop execution if there was an status error.


# Function for identifying Weather based on Latitude and Longitude
def weather(lat, long):
    # Ask user to select the Unit type
    unit = input(
        "\nType '1' for Fahrenheit\nType '2' for Celsius\nType any number for Kelvin\n\n"
    )
    unit_val = input_validation(unit)
    if unit_val != "error":
        match unit_val:
            case 1:
                unit = "imperial"
                unit_name = "Fahrenheit"
                symb = "\N{DEGREE SIGN}" + "F"  # Fahrenheit Symbol
            case 2:
                unit = "metric"
                unit_name = "Celsius"
                symb = "\N{DEGREE SIGN}" + "C"  # Celsius Symbol
            case _:
                unit = "standard"
                unit_name = "Kelvin"
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
            preety_print(weather, unit_name, symb)
        else:
            requests_code(status)
            sys.exit()  # Stop execution if there was an status error.


# Function for displaying Weather information
def preety_print(climate, unit_name, symb):
    print(
        "\nWeather Details\n----------------\nCity: {}\nCountry: {}\nCurrent Temp: {}{}\nFeels Like: {}{}\nMin Temp: {}{}\nMax Temp: {}{}\nHumidity: {}\nPressure: {}\nDescription: {}".format(
            climate["name"],
            climate["sys"]["country"],
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
    while keep_going:
        # Ask User to select the Search type
        option = input(
            "\nType 1 for Search based on City name\nType 2 for Search based on ZIP\nType 'X' to Exit\n\n"
        )
        option_val = input_validation(option)
        if option_val != "error":
            if option_val == 1:
                city = input("Type the City name: ")
                # Calling city search function by passing user typed city value
                city_lat = city_search(city)
                if city_lat is None:
                    print("")
                else:
                    lat, long = city_lat
                    weather(lat, long)

            elif option_val == 2:
                zip = input("Type the Zip code: ")
                country_code = input("Type the two digit country code: ")
                # Calling zip search function by passing user typed zip value
                lat, long = zip_search(zip, country_code)
                weather(lat, long)

            else:
                print("Please select the right option")
                keep_going = False


if __name__ == "__main__":
    main()

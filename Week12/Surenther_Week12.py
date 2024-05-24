# DSC 510
# Week 11
# Programming Assignment Week 12 [ Final Project ]
# Author Surenther Selvaraj

# Change History
# 05/22/2024  Week12 Initial Development         - Surenther Selvaraj

import requests
import json
import sys

app_id = '1b93174e0a0a4f0c8cc7032582e21b6b'

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

# Function for returning error based on Status
def error_code(status):
    if status == 400:
        print ("Error 400 - Bad Request")
    elif status == 401:
        print ("Error 401 - Unauthorized")
    elif status == 404:
        print ("Error 404 - Not Found")
    elif status == 429:
        print ("Error 429 - Quota exceeded")
    else:
        print ("Unexpected error")

# Function for identifying Lattitude and longtitude
def latitude (city):
    url = "http://api.openweathermap.org/geo/1.0/direct?q="+city+"&limit=5"+"&appid="+app_id
    lat = json.loads(req_url(url)[0])
    status = req_url(url)[1]
    city_merge = ""
    if status == 200 :
        if (len(lat)) > 0:
            for key, value in enumerate(lat):
                city = "Type '{}' for {} in {},{}".format(key,value['name'],value['state'],value['country'])
                city_merge = city_merge + "\n" + city
    else:
        error_code(status)
        sys.exit()
    city = input ("".join(city_merge + "\n\nType 'X' to Exit" + "\n \n"))
    if city.lower() == "x":
        print("\n Good Bye \n")
    else:        
        try:
            city_key = int(city)
        except ValueError:
            print("Sorry, that is not an integer . Try again.")
        else:
            if city_key  >= len(lat) :
                print("Please Select right City")
            else:
                return lat[city_key]['lat'] , lat[city_key] ['lon'] , lat[city_key]


def main ():
    Option = input ('please enter city name:')
    print (latitude(Option))

        
if __name__ == "__main__":
    main()

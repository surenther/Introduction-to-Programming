# DSC 510
# Week 10
# Programming Assignment Week 10 [ Web Services ]
# Author Surenther Selvaraj

# Change History
# 05/14/2024  Week10 Assignment Initial Development         - Surenther Selvaraj

import requests
import json
import sys

def main():
    
    call_category = requests.get("https://api.chucknorris.io/jokes/categories")
    categories = json.loads(call_category.text)
    cntr = 1
    category_dict = {}
    for value in categories:
        category_dict [cntr] = value
        cntr = cntr + 1
                
    category = int (input ("Category Selections:\n" + "\n".join("Type '{}' for {}".format(k, v) for k, v in category_dict.items()) + "\n \n"))
    category_value = category_dict.get(category)
    if category_value :
        param = {'category':category_dict [category]}
    else:
        print ('Please Select right Category')
        sys.exit()
    
    call_joke = requests.get("https://api.chucknorris.io/jokes/random",params=param)
    
    joke = json.loads(call_joke.text)
    print ("\n Category Selected: {} \n \n Joke: {} \n".format("" .join(joke ['categories']),joke['value']))
 



if __name__ == "__main__":
    main()
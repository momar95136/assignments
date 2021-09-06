"""
this program will do the following :
Sports Results

Use the following API to retrieve sports results and sort into table of results. Each sport result
contains several data and always includes the publication time.
Method: POST
Content-Type: application/json
Url: https://ancient-wood-1161.getsandbox.com:443/results
Tasks:
- Create python script that displays the sports results in reverse chronological order.
- Add a parameter to the script to display only certain types or events (e.g. f1Results)
- Add a parameter to set the locale (e.g. en)
- How can you confirm the code works?
- Bonus: Implement the rest call asynchronously
"""



""""
Assumptiopns : 
        - The command line will be passed with correct case sensetive arguments [TODO: enhancement]
        - The target endpoint of the service is active & accessable
        - Only implementing the happy path 

"""



from typing import Dict
import requests
import json
import sys
import datetime
import pandas as pd
from tabulate import tabulate


#KEY GLOBAL VARAIBLRES 
KEY =""
RESPONSE_CODE =""
SORT_KEY = ""
headers =  {"Content-Type":"application/json"}
api_url = "https://ancient-wood-1161.getsandbox.com:443/results"
#getting response with headers


#Function to return the response of Post request using the URL & adds headers to the request
def get_response(url, header_information):

    response = requests.post(api_url, headers=headers)
    data = response.json()
    RESPONSE_CODE  = response.status_code
    return [data, RESPONSE_CODE]



#Format the data received yo beautify
def format_output(data):
    print(json.dumps(data, indent=4, sort_keys=True))



#Main program entry points
def main():

    #Get the data based on the URL & Headeres
    [data, RESPONSE_CODE] = get_response(api_url, headers)

    #Print the response code that was returned 
    print("Response Code : {} ".format(RESPONSE_CODE))
    
    #Check for passed paramters at run time 
    count = len(sys.argv)
    if count == 2:
        KEY = sys.argv[1]
        data[KEY].sort(key = lambda i: datetime.datetime.strptime(i["publicationDate"], "%b %d, %Y %I:%M:%S %p"), reverse = True)
        print_tabular_format_for_sport_type(data[KEY])


    elif count == 3:
         KEY = sys.argv[1]
         SORT_KEY  = sys.argv[2]
         data[KEY].sort(key = lambda i: i[SORT_KEY], reverse = True)         
         print_tabular_format_for_sport_type(data[KEY])
    else:

        for key in data.keys():
            print("*" * 20)
            print(key)
            print("*" * 20)
            print_tabular_format_for_sport_type(data[key])
         


#Formating the data based on the key with the assumption that the key exists
def debug(data,key):
    print("=" * 20) 
    print(json.dumps(data[key], indent=4, sort_keys=True))
    print("=" * 20)
    print("\n")


def print_tabular_format_for_sport_type(dataset):
    keys = []
    vals = []
    for data in dataset:
        val = []
        for k,v in data.items():
            keys.append(k)
            val.append(v)
        vals.append(val)

    df = pd.DataFrame([v for v in vals], columns=list(dict.fromkeys(keys)))
    print(tabulate(df, headers='keys', tablefmt='psql'))

def print_type(sports_data):
    if type(sports_data) is dict:
        for i in sports_data.keys():
            print ("Results Type: {}".format(i))

#execute the module
if __name__ == "__main__":
    main()


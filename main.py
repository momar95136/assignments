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

import requests
import json



headers =  {"Content-Type":"application/json"}
api_url = "https://ancient-wood-1161.getsandbox.com:443/results"
#getting response with headers

def get_response(url, header_information):

    response = requests.post(api_url, headers=headers)
    data = response.json()
    response_code = response.status_code
    return data

#resetting syntax to use "" instead of ''

def format_output(data):
    print(json.dumps(data, indent=4, sort_keys=True))

#Traverse

#priniting output
#print(response_code)
def main():
    data = get_response(api_url, headers)
    format_output(data)

#execute the module

if __name__ == "__main__":
    print("hello")
    main()


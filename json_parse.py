#!/usr/bin/python
__author__ = 'brettdeangelis'

"""A module for fetching state geolocation JSON data and printing to text file.
requires Requests module to handle HTTP Request in place of urllib2 module
to install: 'pip install requests'"""
#Handles the http request
import requests
#Handles the JSON object
import json

#URL to gather JSON data
url_base = "http://api.sba.gov/geodata/city_county_links_for_state_of/"
#States list to iterate
states = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]
#output pretty print file
output_file = 'geo_info.txt'

def geo_data_gather():
    geo_list = []
    #For each state in the list gather JSON info
    for state in states:
        #url requires state abbrev to be two letters & lowercase
        full_url = url_base + "{0}.json".format(state.lower())
        #Using the requests object, retrieve the data
        response = requests.get(full_url)
        #Set data variable to the JSON data
        data = response.json()
        #Add each state's info to list for printing
        #json.dumps pretty prints data
        geo_list.append(json.dumps(data, indent=4))
    #Write out list to text file one item per line
    with open(output_file , 'w') as f:
        f.writelines(geo_list)



if __name__ == '__main__':
    geo_data_gather()